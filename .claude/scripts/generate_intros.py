#!/usr/bin/env python3
"""Generate intro markdown for a US Core profile page.

Reads a StructureDefinition JSON snapshot, classifies its elements into
Must Have / Must Support / USCDI buckets, and renders a Jinja2 template.

Usage:
    generate_intros.py SD_JSON [--template PATH] [--polish] [--write]

SD_JSON is the post-snapshot file the IG Publisher writes to output/,
e.g. output/StructureDefinition-us-core-flag.json.
"""

import argparse
import json
import re
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

USCDI_EXTENSION_URL = (
    "http://hl7.org/fhir/us/core/StructureDefinition/uscdi-requirement"
)
W5_AUTHOR_FRAGMENT = "author"

DEFAULT_TEMPLATE = Path(__file__).resolve().parent / "Profile_intro.md.j2"
INTRO_NOTES_DIR = (
    Path(__file__).resolve().parent.parent / "input" / "intro-notes"
)


# ----- element classification -----

def has_uscdi_extension(element):
    for ext in element.get("extension", []) or []:
        if ext.get("url") == USCDI_EXTENSION_URL:
            return True
    return False


def has_w5_author_mapping(element):
    for mapping in element.get("mapping", []) or []:
        if (
            mapping.get("identity") == "w5"
            and W5_AUTHOR_FRAGMENT in (mapping.get("map") or "")
        ):
            return True
    return False


def is_root(element, resource_type):
    return element.get("path") == resource_type


def is_must_have(element, resource_type):
    return (
        not is_root(element, resource_type)
        and element.get("mustSupport") is True
        and (element.get("min") or 0) >= 1
    )


def is_must_support(element, resource_type):
    return (
        not is_root(element, resource_type)
        and element.get("mustSupport") is True
        and (element.get("min") or 0) == 0
        and not has_uscdi_extension(element)
    )


def is_uscdi(element, resource_type):
    return not is_root(element, resource_type) and has_uscdi_extension(element)


# ----- label formatting -----

def is_pipe_separated_codes(short):
    if "|" not in short:
        return False
    s = re.sub(r"^\(US\)\s*", "", short).strip()
    parts = [p.strip().rstrip("+").strip() for p in s.split("|")]
    return all(p and " " not in p for p in parts)


def humanize_element_name(path):
    last = path.rsplit(".", 1)[-1]
    spaced = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", last)
    return spaced.lower()


def format_label(element):
    short = element.get("short") or element.get("path", "")
    short = short.strip().rstrip(".")
    if not short:
        return ""

    if is_pipe_separated_codes(short):
        name = humanize_element_name(element.get("path", ""))
        if not name:
            return ""
        max_val = str(element.get("max", "1"))
        if max_val == "1":
            article = "an" if name[:1] in "aeiou" else "a"
            return f"{article} {name}"
        return f"one or more {name}"

    return short[0].lower() + short[1:]


# ----- context building -----

def build_context(sd, sd_path):
    resource_type = sd.get("type", "")
    elements = (sd.get("snapshot") or {}).get("element", []) or []

    must_have, must_support, uscdi = [], [], []
    has_author = False

    for el in elements:
        if has_w5_author_mapping(el):
            has_author = True

        label = format_label(el)
        if not label:
            continue

        item = {"label": label, "footnote": None}

        if is_must_have(el, resource_type):
            must_have.append(item)
        elif is_uscdi(el, resource_type):
            uscdi.append(item)
        elif is_must_support(el, resource_type):
            must_support.append(item)

    must_have = _dedup_by_label(must_have)
    must_support = _dedup_by_label(must_support)
    uscdi = _dedup_by_label(uscdi)

    return {
        "file_name": sd_path.stem,
        "resource_type": resource_type,
        "must_have": must_have,
        "must_support": must_support,
        "uscdi": uscdi,
        "has_uscdi": bool(uscdi),
        "has_author": has_author,
    }


def _dedup_by_label(items):
    seen = set()
    out = []
    for item in items:
        key = item["label"].strip().lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


# ----- rendering -----

def render(template_path, context):
    template_path = Path(template_path)
    env = Environment(
        loader=FileSystemLoader(str(template_path.parent)),
        undefined=StrictUndefined,
        keep_trailing_newline=True,
    )
    return env.get_template(template_path.name).render(**context)


# ----- optional Anthropic polish -----

POLISH_PROMPT = """You are editing bullet text from a US Core FHIR Implementation Guide. Each bullet describes one data element of the {resource_type} profile and appears under headings like "Each {resource_type} Must Have:" or "Each {resource_type} Must Support:".

Rewrite each `label` as a more natural English phrase that reads well in a bulleted list.

Rules:
- If the label starts with "a ", "an ", or "one or more ", keep that prefix exactly as-is. Do not add a leading article to labels that lack one.
- Preserve meaning exactly. Do not invent details not present in the original.
- Use plain, present-tense English. Prefer common words over jargon.
- Aim for under 12 words. Concision wins.
- Do not capitalize the first letter (these sit mid-sentence under a heading).
- No trailing punctuation.
- If the original already reads naturally, return it unchanged.

Return ONLY a JSON array, no preamble or commentary, shaped like:
[{{"list": "must_have", "index": 0, "polished": "..."}}, ...]

Bullets to polish:
{items_json}
"""


def polish_labels(context, model="claude-sonnet-4-6"):
    from anthropic import Anthropic
    from dotenv import load_dotenv

    load_dotenv()

    items = []
    for list_name in ("must_have", "must_support", "uscdi"):
        for idx, item in enumerate(context[list_name]):
            items.append(
                {"list": list_name, "index": idx, "label": item["label"]}
            )

    if not items:
        return {**context}

    prompt = POLISH_PROMPT.format(
        resource_type=context["resource_type"],
        items_json=json.dumps(items, indent=2),
    )

    client = Anthropic()
    response = client.messages.create(
        model=model,
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )
    raw = response.content[0].text.strip()
    if raw.startswith("```"):
        raw = re.sub(
            r"^```(?:json)?\s*|\s*```$", "", raw, flags=re.MULTILINE
        )
    polished = json.loads(raw)

    new_context = {**context}
    for list_name in ("must_have", "must_support", "uscdi"):
        new_context[list_name] = [dict(item) for item in context[list_name]]
    for entry in polished:
        new_context[entry["list"]][entry["index"]]["label"] = entry["polished"]
    return new_context


# ----- main -----

def main():
    parser = argparse.ArgumentParser(
        description="Generate intro markdown for a US Core profile."
    )
    parser.add_argument(
        "sd_json",
        type=Path,
        help="Path to a StructureDefinition JSON snapshot "
             "(e.g. output/StructureDefinition-us-core-flag.json)",
    )
    parser.add_argument(
        "--template",
        type=Path,
        default=DEFAULT_TEMPLATE,
        help=f"Path to the Jinja2 template (default: {DEFAULT_TEMPLATE})",
    )
    parser.add_argument(
        "--polish",
        action="store_true",
        help="Send bullets through the Anthropic API for rewriting "
             "(requires ANTHROPIC_API_KEY).",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help=f"Write to {INTRO_NOTES_DIR}/<id>-intro.md instead of stdout.",
    )
    args = parser.parse_args()

    with args.sd_json.open() as f:
        sd = json.load(f)

    context = build_context(sd, args.sd_json)
    if args.polish:
        context = polish_labels(context)

    output = render(args.template, context)

    if args.write:
        out_file = INTRO_NOTES_DIR / f"{args.sd_json.stem}-intro.md"
        out_file.write_text(output)
        print(f"wrote {out_file}", file=sys.stderr)
    else:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
