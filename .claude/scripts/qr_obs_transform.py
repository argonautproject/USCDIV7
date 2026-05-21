#!/usr/bin/env python3
"""Transform a FHIR QuestionnaireResponse into a set of US Core Observation
panel + item resources.

Inputs and resources are handled as plain Python dicts loaded from YAML; no
FHIR class library is required. Configuration is read from a YAML file
(default: qr_obs_transform.config.yml next to the script).

Usage:
    python qr_obs_transform.py [--config PATH]
"""
import argparse
import copy
import csv
import re
from pathlib import Path

import yaml

LOINC_CODE_RE = re.compile(r'^\d{1,5}-\d$|^LA\d+-\d$')


# ----- I/O helpers --------------------------------------------------------

def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def dump_yaml(obj, path):
    with open(path, 'w') as f:
        yaml.safe_dump(obj, f, default_flow_style=False, sort_keys=False, width=120)


# ----- Config -------------------------------------------------------------

class Context:
    """Holds loaded config + Questionnaire/QuestionnaireResponse dicts."""

    def __init__(self, cfg):
        self.profile = cfg['profile']
        self.category = cfg['category']
        self.category_path = Path(cfg['category_path'])
        self.survey_name = cfg['survey_name']
        self.survey_code = cfg['survey_code']
        self.survey_code_name = cfg['survey_code_name']
        self.create_survey_panel = cfg.get('create_survey_panel', True)
        self.template_path = Path(cfg['template_path'])
        self.out_dir = Path(cfg['out_dir'])
        self.qr_obj = load_yaml(cfg['qr_path'])
        self.q_obj = load_yaml(cfg['q_path'])
        self.template = load_yaml(self.template_path)
        self.loinc_csv_path = Path(cfg['loinc_csv_path']) if cfg.get('loinc_csv_path') else None
        self._loinc_lcn_cache = None

    def loinc_lcn(self, code):
        """Return the LOINC Long Common Name (LCN) for a parent code, or None.

        Loaded lazily from LoincTableCore.csv if `loinc_csv_path` is configured.
        """
        if not self.loinc_csv_path or not code or not LOINC_CODE_RE.match(code) or code.startswith('LA'):
            return None
        if self._loinc_lcn_cache is None:
            self._loinc_lcn_cache = {}
            with open(self.loinc_csv_path) as f:
                r = csv.reader(f)
                next(r)
                for row in r:
                    self._loinc_lcn_cache[row[0]] = row[9]
        return self._loinc_lcn_cache.get(code)


# ----- Category lookup ----------------------------------------------------

def get_category(ctx):
    """Look up the configured category code in the US Core category CodeSystem.

    Returns a CodeableConcept-shaped dict if found, otherwise None.
    """
    cs = load_yaml(ctx.category_path) if ctx.category_path.suffix in {'.yml', '.yaml'} \
        else __import__('json').load(open(ctx.category_path))
    for cat in cs.get('concept', []):
        if cat.get('code') == ctx.category:
            return {
                'coding': [{
                    'system': cs['url'],
                    'code': cat['code'],
                    'display': cat['display'],
                }]
            }
    return None


# ----- Writers ------------------------------------------------------------

def write_out(ctx, obs):
    out_path = ctx.out_dir / f'Observation-{obs["id"]}.yml'
    dump_yaml(obs, out_path)


def update_members(ctx, parent, members):
    """Re-read a panel Observation and populate its hasMember array."""
    if isinstance(parent, str):
        parent = parent.replace('/', '')
    in_path = ctx.out_dir / f'Observation-{ctx.survey_name}-panel-example-{parent}.yml'
    obs = load_yaml(in_path)
    obs['hasMember'] = [{'reference': f'Observation/{m}'} for m in members]
    write_out(ctx, obs)


# ----- Questionnaire lookups ---------------------------------------------

def get_units(ctx, link_id):
    """Read questionnaire-unit extension on the matching Questionnaire item."""
    target = f'/{link_id}'
    for item in ctx.q_obj.get('item', []):
        if item.get('linkId') == target:
            for ext in item.get('extension', []):
                if ext.get('url') == 'http://hl7.org/fhir/StructureDefinition/questionnaire-unit':
                    return ext.get('valueCoding', {}).get('code')
    return None


def get_help_text(ctx, link_id):
    """Return the help-text display child (if any) on the matching item."""
    target = f'/{link_id}'
    for item in ctx.q_obj.get('item', []):
        if item.get('linkId') == target:
            for child in item.get('item', []) or []:
                if child.get('type') == 'display':
                    return child.get('text')
    return None


# ----- Value builders -----------------------------------------------------

def make_ccode(coding):
    return {
        'coding': [coding],
        'text': coding.get('display'),
    }


def make_quantity(value, units):
    if not units:
        return {'value': value}
    unit_label = units.replace('{', '').replace('}', '').replace('/a', ' per year').strip()
    return {
        'value': value,
        'unit': unit_label,
        'system': 'http://unitsofmeasure.org',
        'code': units,
    }


def apply_answer(ctx, obs, answer):
    if 'valueCoding' in answer:
        obs['valueCodeableConcept'] = make_ccode(answer['valueCoding'])
    elif 'valueString' in answer:
        obs['valueString'] = answer['valueString']
    elif 'valueDecimal' in answer:
        units = get_units(ctx, obs['code']['coding'][0]['code'])
        obs['valueQuantity'] = make_quantity(answer['valueDecimal'], units)
    return obs


# ----- Observation factory ------------------------------------------------

def create_obs(ctx, obs_id, text, obs_type='item', answer=None, code_value=None):
    obs = copy.deepcopy(ctx.template)
    obs['id'] = f'{ctx.survey_name}-{obs_type}-example-{obs_id}'
    obs['meta']['extension'][0]['valueString'] = (
        f'{ctx.survey_name} {obs_type} Example {obs_id}'.title()
    )
    obs['meta']['extension'][1]['valueMarkdown'] = (
        f'This is a {obs["meta"]["extension"][0]["valueString"]} ({text}) '
        f'for the *US Core Observation Screening Assessment Profile*'
    )
    obs['meta']['profile'] = [ctx.profile]

    extra_cat = get_category(ctx)
    if extra_cat:
        obs['category'].append(extra_cat)

    code_for_obs = code_value or obs_id
    lcn = ctx.loinc_lcn(code_for_obs)
    display = lcn or text
    obs['code']['coding'][0]['code'] = code_for_obs
    obs['code']['coding'][0]['display'] = display
    obs['code']['text'] = display

    if answer:
        apply_answer(ctx, obs, answer)
        obs.pop('hasMember', None)
    else:
        obs['hasMember'] = []

    obs['effectiveDateTime'] = ctx.qr_obj.get('authored')
    obs['subject']['reference'] = ctx.qr_obj['subject']['reference']

    author_ref = ctx.qr_obj.get('author', {}).get('reference')
    if author_ref:
        obs.setdefault('performer', [{}])[0]['reference'] = author_ref

    obs['derivedFrom'] = [{
        'reference': f'QuestionnaireResponse/{ctx.qr_obj["id"]}',
    }]
    qr_meta_ext = ctx.qr_obj.get('meta', {}).get('extension', [])
    if qr_meta_ext and 'valueString' in qr_meta_ext[0]:
        obs['derivedFrom'][0]['display'] = qr_meta_ext[0]['valueString']

    help_text = get_help_text(ctx, obs['code']['coding'][0]['code'])
    if help_text:
        obs['note'] = [{'text': help_text}]

    return obs


# ----- Walker -------------------------------------------------------------

def walk_items(ctx, container, parent=None):
    """Recursively walk QR.item, writing one Observation per answered item and
    one panel Observation per group."""
    children = container.get('item')
    if not children:
        return

    member_ids = []
    for child in children:
        link_id = child.get('linkId', '')
        code = link_id.split('/')[-1]
        text = child.get('text', '')
        answers = child.get('answer')

        if not answers:
            if not child.get('item'):
                continue
            panel = create_obs(ctx, code, text, 'panel')
            member_ids.append(panel['id'])
            write_out(ctx, panel)
        elif len(answers) > 1:
            for idx, ans in enumerate(answers):
                multi_code = f'{code}-answer{idx}'
                item = create_obs(ctx, multi_code, text, 'multiselect-item', ans, code_value=code)
                member_ids.append(item['id'])
                write_out(ctx, item)
        else:
            item = create_obs(ctx, code, text, 'item', answers[0])
            member_ids.append(item['id'])
            write_out(ctx, item)

        walk_items(ctx, child, link_id)

    if parent is not None:
        try:
            update_members(ctx, parent, member_ids)
            return
        except FileNotFoundError:
            pass

    if ctx.create_survey_panel:
        survey_panel = create_obs(ctx, ctx.survey_code, ctx.survey_code_name, 'panel')
        write_out(ctx, survey_panel)
        update_members(ctx, ctx.survey_code, member_ids)


# ----- Entrypoint ---------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--config',
        default='qr_obs_transform.config.yml',
        help='Path to YAML configuration (default: next to the script)',
    )
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = Path(__file__).parent / args.config

    cfg = load_yaml(config_path)
    ctx = Context(cfg)
    ctx.out_dir.mkdir(parents=True, exist_ok=True)
    walk_items(ctx, ctx.qr_obj)


if __name__ == '__main__':
    main()
