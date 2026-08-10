#!/usr/bin/env python3
"""Determine which FHIR version first added DocumentReference as a target on a fixed
list of resource elements. Reads core packages from ~/.fhir/packages."""

import csv
import json
import os
import re
import sys
import tarfile
import xml.etree.ElementTree as ET
from pathlib import Path

PACKAGES_DIR = Path(os.path.expanduser("~/.fhir/packages"))
R6_SOURCE_DIR = Path("/Users/ehaas/Documents/FHIR/fhir/source")
FHIR_NS = "{http://hl7.org/fhir}"

# Canonical version ordering.
RELEASE_ORDER = ["R2", "R3", "R4", "R4B", "R5", "R6"]


def map_fhir_version(pkg_version: str):
    v = pkg_version.strip()
    if v.startswith("1.0."):
        return "R2"
    if v.startswith("3.0."):
        return "R3"
    if v == "4.0.1" or v.startswith("4.0."):
        return "R4"
    if v.startswith("4.3."):
        return "R4B"
    if v.startswith("5.0."):
        return "R5"
    if v.startswith("6.0."):
        return "R6"
    return None


# (current_path, current_type)
ELEMENTS = [
    ("AdverseEvent.contributingFactor", "CodeableReference"),
    ("AdverseEvent.mitigatingAction", "CodeableReference"),
    ("AdverseEvent.preventiveAction", "CodeableReference"),
    ("AdverseEvent.supportingInfo", "CodeableReference"),
    ("Appointment.patientInstruction", "CodeableReference"),
    ("Consent.policyText", "Reference"),
    ("Consent.sourceReference", "Reference"),
    ("Contract.friendly.content[x]", "Reference"),
    ("Contract.legal.content[x]", "Reference"),
    ("Contract.legallyBinding[x]", "Reference"),
    ("Contract.rule.content[x]", "Reference"),
    ("Contract.term.action.reason", "CodeableReference"),
    ("DeviceRequest.reason", "CodeableReference"),
    ("DiagnosticReport.media.link", "Reference"),
    ("DiagnosticReport.supportingInfo.reference", "Reference"),
    ("DocumentReference.relatesTo.target", "Reference"),
    ("FamilyMemberHistory.reason", "CodeableReference"),
    ("ImagingSelection.derivedFrom", "Reference"),
    ("ImagingStudy.reason", "CodeableReference"),
    ("MedicinalProductDefinition.attachedDocument", "Reference"),
    ("MedicinalProductDefinition.masterFile", "Reference"),
    ("NutritionIntake.reason", "CodeableReference"),
    ("Observation.derivedFrom", "Reference"),
    ("PackagedProductDefinition.attachedDocument", "Reference"),
    ("Procedure.reason", "CodeableReference"),
    ("Procedure.report", "Reference"),
    ("RegulatedAuthorization.attachedDocument", "Reference"),
    ("RequestOrchestration.reason", "CodeableReference"),
    ("RiskAssessment.reason", "CodeableReference"),
    ("ServiceRequest.basedOn", "Reference"),
    ("ServiceRequest.patientInstruction.instruction[x]", "Reference"),
    ("ServiceRequest.reason", "CodeableReference"),
    ("SubstanceDefinition.code.source", "Reference"),
    ("SubstanceDefinition.name.source", "Reference"),
    ("SubstanceDefinition.relationship.source", "Reference"),
    ("SubstanceDefinition.structure.representation.document", "Reference"),
    ("SubstanceDefinition.structure.sourceDocument", "Reference"),
]

RESOURCE_ALIASES = {
    "RequestOrchestration": ["RequestGroup"],
}

# Element aliases: current_path -> list of alternative paths to try in older versions.
# R5 AdverseEvent kept these as BackboneElement wrappers with a child `.item[x]`
# (Reference|CodeableConcept). R6 collapsed that into a direct CodeableReference on
# the parent path. The DR target therefore lives on the child in R5.
ELEMENT_ALIASES = {
    "AdverseEvent.contributingFactor": [
        "AdverseEvent.contributingFactor.item[x]",
        "AdverseEvent.contributor",
    ],
    "AdverseEvent.mitigatingAction": [
        "AdverseEvent.mitigatingAction.item[x]",
    ],
    "AdverseEvent.preventiveAction": [
        "AdverseEvent.preventiveAction.item[x]",
    ],
    "AdverseEvent.supportingInfo": [
        "AdverseEvent.supportingInfo.item[x]",
    ],
    "Appointment.patientInstruction": ["Appointment.patientInstruction"],
    "Consent.sourceReference": [
        "Consent.source[x]",
        "Consent.sourceReference",
        "Consent.sourceAttachment",
    ],
    "DeviceRequest.reason": [
        "DeviceRequest.reasonReference",
        "DeviceRequest.reason[x]",
    ],
    "FamilyMemberHistory.reason": [
        "FamilyMemberHistory.reasonReference",
        "FamilyMemberHistory.reason[x]",
    ],
    "ImagingStudy.reason": [
        "ImagingStudy.reasonReference",
        "ImagingStudy.reason[x]",
    ],
    "NutritionIntake.reason": [
        "NutritionIntake.reasonReference",
        "NutritionOrder.reasonReference",
        "NutritionIntake.reason[x]",
    ],
    "Procedure.reason": ["Procedure.reasonReference", "Procedure.reason[x]"],
    "RequestOrchestration.reason": [
        "RequestGroup.reasonReference",
        "RequestGroup.reason[x]",
    ],
    "RiskAssessment.reason": [
        "RiskAssessment.reasonReference",
        "RiskAssessment.reason[x]",
    ],
    "ServiceRequest.reason": [
        "ServiceRequest.reasonReference",
        "ServiceRequest.reason[x]",
    ],
    "Contract.term.action.reason": [
        "Contract.term.action.reasonReference",
        "Contract.term.action.reason[x]",
    ],
}

DR_CANONICAL = "http://hl7.org/fhir/StructureDefinition/DocumentReference"


def discover_core_packages():
    """Yield (release_label, pkg_version, sd_loader). sd_loader is a dict resource_name -> json dict."""
    if not PACKAGES_DIR.exists():
        print(f"ERROR: packages dir does not exist: {PACKAGES_DIR}", file=sys.stderr)
        sys.exit(2)
    entries = sorted(PACKAGES_DIR.iterdir())
    found = []
    for entry in entries:
        if entry.is_dir():
            pkg_json_path = entry / "package" / "package.json"
            if not pkg_json_path.is_file():
                continue
            try:
                meta = json.loads(pkg_json_path.read_text())
            except Exception:
                continue
            name = meta.get("name", "")
            if not re.match(r"^hl7\.fhir\.r[0-9a-zA-Z]+\.core$", name):
                continue
            version = meta.get("version", "")
            release = map_fhir_version(version)
            if release is None:
                continue
            found.append((release, version, name, entry))
        elif entry.suffix == ".tgz" or entry.name.endswith(".tar.gz"):
            try:
                with tarfile.open(entry, "r:gz") as tf:
                    member = None
                    for m in tf.getmembers():
                        if m.name.endswith("package/package.json") or m.name == "package/package.json":
                            member = m
                            break
                    if member is None:
                        continue
                    f = tf.extractfile(member)
                    meta = json.loads(f.read().decode())
                    name = meta.get("name", "")
                    if not re.match(r"^hl7\.fhir\.r[0-9a-zA-Z]+\.core$", name):
                        continue
                    version = meta.get("version", "")
                    release = map_fhir_version(version)
                    if release is None:
                        continue
                    found.append((release, version, name, entry))
            except Exception:
                continue
    return found


def _xml_val(el, tag):
    child = el.find(FHIR_NS + tag)
    if child is None:
        return None
    return child.get("value")


def load_r6_source_sds(source_dir: Path):
    """Walk source_dir for structuredefinition-*.xml that define resource SDs and
    return dict resource_type -> pseudo-SD dict shaped like the JSON form
    (with differential.element[].path and type[].code/targetProfile).
    Only resource SDs (kind=resource) are returned."""
    sds = {}
    if not source_dir.is_dir():
        return sds
    for xf in source_dir.glob("*/structuredefinition-*.xml"):
        try:
            tree = ET.parse(xf)
        except ET.ParseError:
            continue
        root = tree.getroot()
        if root.tag != FHIR_NS + "StructureDefinition":
            continue
        kind = _xml_val(root, "kind")
        if kind != "resource":
            continue
        # Only the resource definition itself, not profiles/examples of it.
        if _xml_val(root, "derivation") != "specialization":
            continue
        rtype = _xml_val(root, "type")
        if not rtype:
            continue
        # Build pseudo-SD with differential.element list.
        diff = root.find(FHIR_NS + "differential")
        elements = []
        if diff is not None:
            for el in diff.findall(FHIR_NS + "element"):
                path = _xml_val(el, "path")
                if not path:
                    continue
                types = []
                for te in el.findall(FHIR_NS + "type"):
                    code = _xml_val(te, "code")
                    tps = [tp.get("value") for tp in te.findall(FHIR_NS + "targetProfile") if tp.get("value")]
                    profs = [p.get("value") for p in te.findall(FHIR_NS + "profile") if p.get("value")]
                    type_entry = {"code": code}
                    if tps:
                        type_entry["targetProfile"] = tps
                    if profs:
                        type_entry["profile"] = profs
                    types.append(type_entry)
                e_dict = {"path": path}
                if types:
                    e_dict["type"] = types
                elements.append(e_dict)
        sd = {
            "resourceType": "StructureDefinition",
            "kind": "resource",
            "type": rtype,
            "differential": {"element": elements},
        }
        if rtype not in sds:
            sds[rtype] = sd
    return sds


def load_resource_sds(pkg_path: Path):
    """Return dict: resource_type -> StructureDefinition JSON."""
    sds = {}
    if pkg_path.is_dir():
        pkg_dir = pkg_path / "package"
        for jf in pkg_dir.glob("*.json"):
            try:
                data = json.loads(jf.read_text())
            except Exception:
                continue
            if not isinstance(data, dict):
                continue
            if data.get("resourceType") != "StructureDefinition":
                continue
            if data.get("kind") != "resource":
                continue
            t = data.get("type")
            if t:
                # prefer first; if dup, keep
                if t not in sds:
                    sds[t] = data
    elif pkg_path.suffix == ".tgz" or pkg_path.name.endswith(".tar.gz"):
        with tarfile.open(pkg_path, "r:gz") as tf:
            for m in tf.getmembers():
                if not m.name.endswith(".json"):
                    continue
                if "/package/" not in m.name and not m.name.startswith("package/"):
                    continue
                try:
                    f = tf.extractfile(m)
                    data = json.loads(f.read().decode())
                except Exception:
                    continue
                if not isinstance(data, dict):
                    continue
                if data.get("resourceType") != "StructureDefinition":
                    continue
                if data.get("kind") != "resource":
                    continue
                t = data.get("type")
                if t and t not in sds:
                    sds[t] = data
    return sds


def get_elements(sd):
    snap = (sd.get("snapshot") or {}).get("element") or []
    if snap:
        return snap, "snapshot"
    diff = (sd.get("differential") or {}).get("element") or []
    return diff, "differential"


def strip_version(url):
    if not url:
        return ""
    return url.split("|", 1)[0]


def collect_target_profiles(type_entries):
    """Return the de-duplicated list of target profile canonicals across all
    Reference/CodeableReference type entries on an element."""
    targets = []
    for t in type_entries or []:
        code = t.get("code")
        if code not in ("Reference", "CodeableReference"):
            continue
        # R4+ : targetProfile is array; STU3: string; DSTU2: profile array on Reference.
        tp = t.get("targetProfile")
        if isinstance(tp, list):
            for x in tp:
                targets.append(strip_version(x))
        elif isinstance(tp, str):
            targets.append(strip_version(tp))
        prof = t.get("profile")
        if isinstance(prof, list):
            for x in prof:
                targets.append(strip_version(x))
        elif isinstance(prof, str):
            targets.append(strip_version(prof))
    # de-dup, preserving order
    seen = set()
    out = []
    for u in targets:
        if u and u not in seen:
            seen.add(u)
            out.append(u)
    return out


def type_targets_dr(type_entries):
    """Return True if any Reference/CodeableReference type entry targets DocumentReference."""
    return DR_CANONICAL in collect_target_profiles(type_entries)


def is_sole_dr_target(type_entries):
    """Return True if DocumentReference is the only target profile listed."""
    targets = collect_target_profiles(type_entries)
    return targets == [DR_CANONICAL]


def find_element_by_path(elements, path):
    """Return the first ElementDefinition with this exact path, or None."""
    for e in elements:
        if e.get("path") == path:
            return e
    return None


def find_element_choice_variants(elements, base_path):
    """For a base path like 'Foo.bar', find any element with path matching:
       Foo.bar[x], Foo.barReference, Foo.barAttachment, etc.
       Return list of (path, element)."""
    out = []
    prefix = base_path
    for e in elements:
        p = e.get("path") or ""
        if p == prefix + "[x]":
            out.append((p, e))
        elif p.startswith(prefix) and p != prefix:
            # e.g. Consent.sourceReference, Consent.sourceAttachment
            tail = p[len(prefix):]
            if tail and tail[0].isupper():
                out.append((p, e))
    return out


def resolve_in_version(sd_map, resource, current_path, current_type):
    """Return (status, matched_path, match_type, type_entries) where status is
    HAS_DR | NO_DR | ELEMENT_ABSENT | RESOURCE_ABSENT. type_entries is the matched
    element's `type` list (or None)."""
    # 1) Resolve resource (apply alias if needed).
    used_resource_alias = False
    sd = sd_map.get(resource)
    if sd is None:
        for alias in RESOURCE_ALIASES.get(resource, []):
            if alias in sd_map:
                sd = sd_map[alias]
                used_resource_alias = True
                break
    if sd is None:
        return "RESOURCE_ABSENT", "", "n/a", None

    elements, _ = get_elements(sd)
    if not elements:
        return "ELEMENT_ABSENT", "", "n/a", None

    # Build candidate paths to try in order.
    candidates = []
    # 1. exact
    candidates.append((current_path, "exact"))
    # 2. resource alias -> rewrite resource prefix
    if used_resource_alias:
        alias_resource = sd.get("type")
        rewritten = alias_resource + current_path[len(resource):]
        candidates.append((rewritten, "resource_alias"))
    # 3. element aliases
    for alt in ELEMENT_ALIASES.get(current_path, []):
        if used_resource_alias:
            alias_resource = sd.get("type")
            # Replace original resource prefix in alt with alias resource if it starts with current resource
            if alt.startswith(resource + "."):
                alt_alias = alias_resource + alt[len(resource):]
                candidates.append((alt_alias, "element_alias"))
            else:
                candidates.append((alt, "element_alias"))
        else:
            candidates.append((alt, "element_alias"))

    tried = set()

    # Try each candidate.
    for path, mtype in candidates:
        if path in tried:
            continue
        tried.add(path)
        # Direct hit
        e = find_element_by_path(elements, path)
        if e is not None:
            if type_targets_dr(e.get("type")):
                label = mtype if not used_resource_alias else "resource_alias+" + mtype
                return "HAS_DR", path, label, e.get("type")
            else:
                # Found element; for CodeableReference current target, we still want
                # to check if it has DR via Reference alone. Keep looking for HAS_DR
                # in other candidates, but remember NO_DR.
                pass
        # If path ends with [x], also probe expanded variants.
        if path.endswith("[x]"):
            base = path[:-3]
            variants = find_element_choice_variants(elements, base)
            for vp, ve in variants:
                if type_targets_dr(ve.get("type")):
                    label = "element_alias" if mtype == "element_alias" else mtype
                    if used_resource_alias:
                        label = "resource_alias+" + label
                    return "HAS_DR", vp, label, ve.get("type")

    # 4. Auto-detect fallback: same (aliased) resource, leaf match or <base>Reference / <base>[x]
    current_leaf = current_path.rsplit(".", 1)[-1]
    is_cr = current_type == "CodeableReference"
    base_path = current_path  # used to compute <base>Reference
    base_leaf = current_leaf

    # Compute the parent-relative path under the resolved SD resource name
    sd_resource = sd.get("type")

    auto_candidates = set()
    # leaf match anywhere in resource
    for e in elements:
        p = e.get("path") or ""
        if p == sd_resource:
            continue
        leaf = p.rsplit(".", 1)[-1]
        if leaf == current_leaf:
            auto_candidates.add(p)
        # <base>Reference / <base>[x] under same parent (if CodeableReference)
        if is_cr:
            # match if leaf is current_leaf+"Reference" or current_leaf+"[x]"
            if leaf == current_leaf + "Reference":
                auto_candidates.add(p)
            if leaf == current_leaf + "[x]":
                auto_candidates.add(p)

    # Try auto candidates for HAS_DR.
    found_no_dr = False
    for path in auto_candidates:
        if path in tried:
            continue
        tried.add(path)
        e = find_element_by_path(elements, path)
        if e is None:
            continue
        if type_targets_dr(e.get("type")):
            label = "resource_alias+auto" if used_resource_alias else "auto"
            return "HAS_DR", path, label, e.get("type")
        else:
            found_no_dr = True

    # Re-check exact/aliases for NO_DR presence (element exists but no DR).
    rep_element = None
    for path in tried:
        e = find_element_by_path(elements, path)
        if e is not None:
            rep_element = (path, e)
            break
    if rep_element or found_no_dr:
        rep_path = rep_element[0] if rep_element else next(iter(tried), current_path)
        rep_types = rep_element[1].get("type") if rep_element else None
        label = "exact" if rep_path == current_path else "element_alias"
        if used_resource_alias:
            label = "resource_alias+" + label
        return "NO_DR", rep_path, label, rep_types

    return "ELEMENT_ABSENT", "", "n/a", None


def main():
    if not PACKAGES_DIR.exists() or not any(PACKAGES_DIR.iterdir()):
        print(f"ERROR: packages dir empty or missing: {PACKAGES_DIR}", file=sys.stderr)
        sys.exit(2)

    discovered = discover_core_packages()
    if not discovered:
        print("ERROR: no core FHIR packages found.", file=sys.stderr)
        sys.exit(2)

    # Keep latest version per release.
    by_release = {}
    for release, version, name, path in discovered:
        if release not in by_release:
            by_release[release] = (version, name, path)

    # R6 from source XML (overrides any package-based R6 if both exist).
    r6_sds_from_source = None
    if R6_SOURCE_DIR.is_dir():
        r6_sds_from_source = load_r6_source_sds(R6_SOURCE_DIR)
        by_release["R6"] = ("6.0.0 (source)", "hl7-fhir-source", R6_SOURCE_DIR)

    print("Discovered core packages:")
    for r in RELEASE_ORDER:
        if r in by_release:
            v, n, p = by_release[r]
            print(f"  {r:4s} <- {n}@{v}  ({p.name})")
        else:
            print(f"  {r:4s} <- (not present)")
    print()

    # Load SDs per release.
    sd_per_release = {}
    for r, (v, n, p) in by_release.items():
        if r == "R6" and r6_sds_from_source is not None:
            print(f"Loading R6 SDs from source XML ({p}) ...", file=sys.stderr)
            sd_per_release[r] = r6_sds_from_source
        else:
            print(f"Loading SDs for {r} ({n}@{v}) ...", file=sys.stderr)
            sd_per_release[r] = load_resource_sds(p)
    print(file=sys.stderr)

    # Releases we will iterate (only those present).
    present_releases = [r for r in RELEASE_ORDER if r in by_release]

    rows = []
    auto_flags = []

    for current_path, current_type in ELEMENTS:
        resource = current_path.split(".", 1)[0]

        per_release_status = {}
        per_release_match = {}  # (matched_path, match_type, type_entries)

        for r in present_releases:
            status, mpath, mtype, type_entries = resolve_in_version(
                sd_per_release[r], resource, current_path, current_type
            )
            per_release_status[r] = status
            per_release_match[r] = (mpath, mtype, type_entries)

        # Build presence trail across ALL canonical releases (including absent ones).
        trail_parts = []
        for r in RELEASE_ORDER:
            if r in per_release_status:
                s = per_release_status[r]
                tag = {"HAS_DR": "has_dr", "NO_DR": "no_dr",
                       "ELEMENT_ABSENT": "elem_absent",
                       "RESOURCE_ABSENT": "res_absent"}[s]
                trail_parts.append(f"{r}:{tag}")
            else:
                trail_parts.append(f"{r}:unknown")
        presence_trail = ";".join(trail_parts)

        # Determine version_added walking R4 → R5 → R6 in order.
        r4_status = per_release_status.get("R4")
        r5_status = per_release_status.get("R5")
        r6_status = per_release_status.get("R6")

        version_added = ""
        package_version_added = ""
        prior_state = ""
        matched_path_in_added = ""
        match_type = ""
        notes = ""
        sole_type_entries = None

        if r4_status == "HAS_DR":
            version_added = "≤ R4"
            package_version_added = by_release["R4"][0]
            mpath, mtype, mtypes = per_release_match["R4"]
            matched_path_in_added = mpath
            match_type = mtype
            sole_type_entries = mtypes
            prior_state = "earlier_release_unavailable"
            notes = "Present in earliest available core (R4); pre-R4 packages not analyzed."
        elif r5_status == "HAS_DR":
            version_added = "R5"
            package_version_added = by_release["R5"][0]
            mpath, mtype, mtypes = per_release_match["R5"]
            matched_path_in_added = mpath
            match_type = mtype
            sole_type_entries = mtypes
            if r4_status == "NO_DR":
                prior_state = "no_dr"
            elif r4_status == "ELEMENT_ABSENT":
                prior_state = "element_absent"
            elif r4_status == "RESOURCE_ABSENT":
                prior_state = "resource_absent"
            else:
                prior_state = "unknown"
            notes = ""
        elif r6_status == "HAS_DR":
            version_added = "R6"
            package_version_added = by_release["R6"][0] if "R6" in by_release else ""
            mpath, mtype, mtypes = per_release_match["R6"]
            matched_path_in_added = mpath
            match_type = mtype
            sole_type_entries = mtypes
            if r5_status == "NO_DR":
                prior_state = "no_dr"
            elif r5_status == "ELEMENT_ABSENT":
                prior_state = "element_absent"
            elif r5_status == "RESOURCE_ABSENT":
                prior_state = "resource_absent"
            else:
                prior_state = "unknown"
            notes = "R6 source: differential only — snapshot not consulted."
        else:
            version_added = "not found"
            package_version_added = ""
            matched_path_in_added = ""
            match_type = "n/a"
            if r6_status == "NO_DR":
                prior_state = "no_dr"
            elif r6_status == "ELEMENT_ABSENT":
                prior_state = "element_absent"
            elif r6_status == "RESOURCE_ABSENT":
                prior_state = "resource_absent"
            else:
                prior_state = "unknown"
            notes = "DR target not found in R4, R5, or R6 source."

        if sole_type_entries is not None:
            is_sole = "yes" if is_sole_dr_target(sole_type_entries) else "no"
        else:
            is_sole = "unknown"

        # Confidence: high unless any relevant match was 'auto'.
        relevant_matches = []
        if r4_status in ("HAS_DR", "NO_DR"):
            relevant_matches.append(per_release_match["R4"][1])
        if r5_status in ("HAS_DR", "NO_DR"):
            relevant_matches.append(per_release_match["R5"][1])
        if r6_status in ("HAS_DR", "NO_DR"):
            relevant_matches.append(per_release_match["R6"][1])
        confidence = "high"
        if any("auto" in m for m in relevant_matches):
            confidence = "low"
            auto_flags.append((resource, current_path, relevant_matches))

        rows.append({
            "resource": resource,
            "element": current_path,
            "r6_type": current_type,
            "version_added": version_added,
            "package_version_added": package_version_added,
            "prior_state": prior_state,
            "matched_path_in_added_version": matched_path_in_added,
            "match_type": match_type,
            "is_sole_target": is_sole,
            "presence_trail": presence_trail,
            "confidence": confidence,
            "notes": notes,
        })

    # Write CSV.
    csv_path = Path("dr_target_version_added.csv")
    fieldnames = [
        "resource", "element", "r6_type", "version_added",
        "package_version_added", "prior_state",
        "matched_path_in_added_version", "match_type",
        "is_sole_target",
        "presence_trail", "confidence", "notes",
    ]
    with csv_path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in rows:
            w.writerow(row)
    print(f"Wrote {csv_path} ({len(rows)} rows).", file=sys.stderr)

    # Markdown summary to both stdout and a file.
    md_lines = []
    md_lines.append("## DocumentReference target — version added (summary)\n")
    md_lines.append("| # | Resource | Element | Version added | Prior state | Is Sole Target | Confidence |")
    md_lines.append("|---|---|---|---|---|---|---|")
    sole_glyph = {"yes": "✓", "no": "", "unknown": "?"}
    for i, r in enumerate(rows, start=1):
        md_lines.append(
            f"| {i} | {r['resource']} | `{r['element']}` | {r['version_added']} | "
            f"{r['prior_state']} | {sole_glyph[r['is_sole_target']]} | {r['confidence']} |"
        )

    if auto_flags:
        md_lines.append("")
        md_lines.append("## Low-confidence (auto-resolved) rows for manual review\n")
        for res, path, matches in auto_flags:
            md_lines.append(f"- **{path}** — auto match types: {matches}")
    else:
        md_lines.append("")
        md_lines.append("_No low-confidence (auto-resolved) rows._")

    md_text = "\n".join(md_lines) + "\n"
    print()
    print(md_text)
    md_path = Path("dr_target_version_added.md")
    md_path.write_text(md_text)
    print(f"Wrote {md_path}.", file=sys.stderr)

    # Second markdown: only R6-added rows.
    r6_rows = [r for r in rows if r["version_added"] == "R6"]
    r6_lines = []
    r6_lines.append("## DocumentReference target — added in R6\n")
    if not r6_rows:
        r6_lines.append("_No elements first added a DocumentReference target in R6._")
    else:
        r6_lines.append("| # | Resource | Element | R6 type | Prior state | Is Sole Target | Matched path | Confidence |")
        r6_lines.append("|---|---|---|---|---|---|---|---|")
        for i, r in enumerate(r6_rows, start=1):
            r6_lines.append(
                f"| {i} | {r['resource']} | `{r['element']}` | {r['r6_type']} | "
                f"{r['prior_state']} | {sole_glyph[r['is_sole_target']]} | "
                f"`{r['matched_path_in_added_version']}` | {r['confidence']} |"
            )
    r6_text = "\n".join(r6_lines) + "\n"
    r6_path = Path("dr_target_version_added_r6.md")
    r6_path.write_text(r6_text)
    print(f"Wrote {r6_path} ({len(r6_rows)} rows).", file=sys.stderr)


if __name__ == "__main__":
    main()
