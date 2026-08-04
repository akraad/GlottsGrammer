#!/usr/bin/env python3
"""
GlottsGrammer Validation Script
--------------------------------
Validates the structure and cross-references of the grammar content repository.

Checks performed:
  1. All config JSON files parse correctly.
  2. All grammar base.json files parse and contain required fields.
  3. All vocab base.json files parse and contain required fields.
  4. Every grammar point references only valid locales, CEFR levels, and universal concepts.
  5. Every grammar point references only vocab IDs that exist in the repository.
  6. Every grammar point has an i18n directory with a JSON file for every configured locale.
  7. Each i18n JSON file parses correctly and contains the locale it claims to represent.
  8. Each i18n JSON has example_translations for all examples in base.
  9. Each i18n JSON has common_error_explanations for all common_errors in base.
 10. Each i18n JSON has vocab_glosses for all vocab references in base.
 11. All prerequisite references point to existing grammar points.

Usage:
  python3 scripts/validate.py
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = ROOT / "config"
CONTENT_DIR = ROOT / "content"


def load_json(path: Path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    # ---- 1. Load config files -------------------------------------------------
    try:
        locales = load_json(CONFIG_DIR / "locales.json")
        locale_codes = {loc["code"] for loc in locales}
    except Exception as e:
        errors.append(f"Failed to load config/locales.json: {e}")
        locale_codes = set()

    try:
        levels = load_json(CONFIG_DIR / "levels.json")
        cefr_levels = {lv["cefr"] for lv in levels}
    except Exception as e:
        errors.append(f"Failed to load config/levels.json: {e}")
        cefr_levels = set()

    try:
        concepts = load_json(CONFIG_DIR / "universal-concepts.json")
        concept_ids = {c["id"] for c in concepts}
    except Exception as e:
        errors.append(f"Failed to load config/universal-concepts.json: {e}")
        concept_ids = set()

    try:
        categories = load_json(CONFIG_DIR / "categories.json")
        category_ids = {c["id"] for c in categories}
    except Exception as e:
        errors.append(f"Failed to load config/categories.json: {e}")
        category_ids = set()

    # ---- 2. Collect all vocab IDs --------------------------------------------
    vocab_ids: set[str] = set()
    for vocab_file in CONTENT_DIR.rglob("vocab/**/base.json"):
        try:
            v = load_json(vocab_file)
            vocab_ids.add(v["id"])
        except Exception as e:
            errors.append(f"Failed to parse vocab file {vocab_file}: {e}")

    # ---- 3. First pass: collect all grammar point IDs ------------------------
    grammar_point_ids: set[str] = set()
    for base_file in CONTENT_DIR.rglob("grammar/**/base.json"):
        try:
            g = load_json(base_file)
            grammar_point_ids.add(g.get("id", ""))
        except Exception:
            pass  # Will be reported in second pass

    # ---- 4. Second pass: full validation -------------------------------------
    for base_file in CONTENT_DIR.rglob("grammar/**/base.json"):
        try:
            g = load_json(base_file)
        except Exception as e:
            errors.append(f"Failed to parse {base_file}: {e}")
            continue

        required_fields = [
            "schema_version", "id", "universal_concept_id", "language",
            "cefr", "app_level", "category", "status", "difficulty",
            "prerequisites", "forms", "examples", "vocab"
        ]
        for field in required_fields:
            if field not in g:
                errors.append(f"{base_file}: missing required field '{field}'")

        gp_id = g.get("id", "<unknown>")

        lang = g.get("language")
        if lang and lang not in locale_codes:
            errors.append(f"{base_file}: invalid language '{lang}'")

        cefr = g.get("cefr")
        if cefr and cefr not in cefr_levels:
            errors.append(f"{base_file}: invalid cefr '{cefr}'")

        uc_id = g.get("universal_concept_id")
        if uc_id and uc_id not in concept_ids:
            errors.append(f"{base_file}: unknown universal_concept_id '{uc_id}'")

        cat = g.get("category")
        if cat and cat not in category_ids:
            warnings.append(f"{base_file}: category '{cat}' not in categories.json")

        # Prerequisites
        for prereq in g.get("prerequisites", []):
            if prereq not in grammar_point_ids:
                warnings.append(f"{gp_id}: prerequisite '{prereq}' not found")

        # Vocab references
        for vocab_ref in g.get("vocab", []):
            if vocab_ref not in vocab_ids:
                errors.append(f"{base_file}: references missing vocab ID '{vocab_ref}'")

        # Collect example IDs and error IDs for cross-reference
        example_ids = {e["id"] for e in g.get("examples", []) if "id" in e}
        error_ids = {e["id"] for e in g.get("common_errors", []) if "id" in e}
        vocab_refs = set(g.get("vocab", []))

        # Check i18n directory
        i18n_dir = base_file.parent / "i18n"
        if not i18n_dir.is_dir():
            errors.append(f"{base_file}: missing i18n directory at {i18n_dir}")
        else:
            found_locales = set()
            for loc in locale_codes:
                loc_file = i18n_dir / f"{loc}.json"
                if not loc_file.exists():
                    errors.append(f"{base_file}: missing i18n file for locale '{loc}'")
                else:
                    found_locales.add(loc)
                    try:
                        t = load_json(loc_file)
                        if t.get("locale") != loc:
                            errors.append(
                                f"{loc_file}: 'locale' field is '{t.get('locale')}', expected '{loc}'"
                            )

                        # Cross-reference example_translations
                        et_keys = set(t.get("example_translations", {}).keys())
                        missing_ex = example_ids - et_keys
                        if missing_ex:
                            warnings.append(
                                f"{gp_id}/{loc}: missing example translations {sorted(missing_ex)}"
                            )

                        # Cross-reference common_error_explanations
                        ce_keys = set(t.get("common_error_explanations", {}).keys())
                        missing_err = error_ids - ce_keys
                        if missing_err:
                            warnings.append(
                                f"{gp_id}/{loc}: missing error explanations {sorted(missing_err)}"
                            )

                        # Cross-reference vocab_glosses
                        vg_keys = set(t.get("vocab_glosses", {}).keys())
                        missing_vg = vocab_refs - vg_keys
                        if missing_vg:
                            warnings.append(
                                f"{gp_id}/{loc}: missing vocab glosses {sorted(missing_vg)}"
                            )

                    except Exception as e:
                        errors.append(f"Failed to parse {loc_file}: {e}")

    # ---- 5. Report -----------------------------------------------------------
    print("=" * 70)
    print("GlottsGrammer Validation Report")
    print("=" * 70)
    print(f"Locales:   {len(locale_codes)}")
    print(f"Levels:    {len(cefr_levels)}")
    print(f"Concepts:  {len(concept_ids)}")
    print(f"Categories:{len(category_ids)}")
    print(f"Vocab:     {len(vocab_ids)}")
    print(f"Grammar:   {len(grammar_point_ids)}")
    print()

    if errors:
        print(f"❌ ERRORS ({len(errors)}):")
        for err in errors:
            print(f"  - {err}")
        print()

    if warnings:
        print(f"⚠️  WARNINGS ({len(warnings)}):")
        for warn in warnings:
            print(f"  - {warn}")
        print()

    if not errors and not warnings:
        print("✅ Validation passed. No errors or warnings.")
        return 0
    elif not errors:
        print("⚠️  Validation passed with warnings.")
        return 0
    else:
        print("❌ Validation FAILED.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
