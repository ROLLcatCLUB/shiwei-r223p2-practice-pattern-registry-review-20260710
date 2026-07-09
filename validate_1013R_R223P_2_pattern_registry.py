import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "R223P_2_art_practice_pattern_registry.json",
    "R223P_2_art_practice_pattern_registry.md",
    "R223P_2_demonstration_type_registry.json",
    "R223P_2_micro_practice_type_registry.json",
    "R223P_2_appreciation_scaffold_type_registry.json",
    "R223P_2_aesthetic_language_focus_registry.json",
    "R223P_2_pattern_relation_map.md",
    "R223P_2_pattern_to_screen_component_evidence_mapping.md",
    "R223P_2_pattern_to_unit_intensity_router_mapping.md",
    "R223P_2_teacher_default_vs_review_ledger_policy.md",
    "R223P_2_registry_validation_report.md",
    "PACKAGE_MANIFEST.json",
    "README_FOR_GPT_REVIEW.md",
]

REQUIRED_PATTERNS = [
    "observation_discovery",
    "comparison_judgment",
    "artwork_appreciation",
    "teacher_demonstration",
    "micro_practice",
    "material_experiment",
    "idea_generation",
    "creation_progression",
    "showcase_evaluation",
    "closure_transfer",
]

REQUIRED_PATTERN_KEYS = [
    "pattern_id",
    "cn_label",
    "layer",
    "core_function",
    "student_problem_solved",
    "suitable_lesson_types",
    "suitable_grade_bands",
    "common_lesson_position",
    "typical_teacher_moves",
    "expected_student_responses",
    "likely_misconceptions_or_failures",
    "teacher_follow_up_or_rescue",
    "screen_trigger_candidates",
    "component_trigger_candidates",
    "learning_sheet_fields",
    "evidence_outputs",
    "assessment_alignment",
    "misuse_risks",
    "relation_to_unit_lesson_practice_intensity_router",
    "teacher_default_view_policy",
    "review_ledger_policy",
    "source_basis",
]

FORBIDDEN_TEXT = [
    "schema_v0_2_published\": true",
    "r97b_modified\": true",
    "formal_ui\": true",
    "runtime_connected\": true",
    "provider_model_connected\": true",
    "database_written\": true",
    "formal_apply\": true",
    "general_pedagogy_core\"",
    "science_experiment",
    "math_variation",
    "chinese_reading",
]


def read_text(name):
    return (ROOT / name).read_text(encoding="utf-8")


def load_json(name):
    return json.loads(read_text(name))


def main():
    checks = []
    failures = []

    for file_name in REQUIRED_FILES:
        ok = (ROOT / file_name).exists()
        checks.append({"check": f"required_file:{file_name}", "passed": ok})
        if not ok:
            failures.append(f"missing {file_name}")

    manifest = load_json("PACKAGE_MANIFEST.json")
    checks.append({"check": "manifest_decision", "passed": manifest.get("decision") == "PASS_CONTINUE_TO_R223P_3_SCHEMA_V0_2_DELTA"})
    boundary = manifest.get("boundary", {})
    for key in [
        "schema_v0_2_published",
        "r223m_p5_schema_modified",
        "r222d_component_library_modified",
        "existing_teacher_drafts_modified",
        "formal_ui",
        "r97b_modified",
        "frontend_backend_modified",
        "runtime_connected",
        "provider_model_connected",
        "prompt_modified",
        "database_written",
        "formal_apply",
    ]:
        ok = boundary.get(key) is False
        checks.append({"check": f"boundary_false:{key}", "passed": ok})
        if not ok:
            failures.append(f"boundary not false: {key}")

    registry = load_json("R223P_2_art_practice_pattern_registry.json")
    patterns = registry.get("patterns", [])
    pattern_by_id = {p.get("pattern_id"): p for p in patterns}
    checks.append({"check": "pattern_count_10", "passed": len(pattern_by_id) == 10})

    for pattern_id in REQUIRED_PATTERNS:
        item = pattern_by_id.get(pattern_id)
        ok = item is not None
        checks.append({"check": f"pattern_exists:{pattern_id}", "passed": ok})
        if not ok:
            failures.append(f"missing pattern {pattern_id}")
            continue
        for key in REQUIRED_PATTERN_KEYS:
            value = item.get(key)
            ok = value not in (None, "", [])
            checks.append({"check": f"pattern_key:{pattern_id}:{key}", "passed": ok})
            if not ok:
                failures.append(f"missing {key} in {pattern_id}")
        ok = item.get("layer") == "art_subject_adapter"
        checks.append({"check": f"pattern_layer:{pattern_id}", "passed": ok})
        if not ok:
            failures.append(f"bad layer in {pattern_id}")

    for file_name, min_count in [
        ("R223P_2_demonstration_type_registry.json", 12),
        ("R223P_2_micro_practice_type_registry.json", 11),
        ("R223P_2_appreciation_scaffold_type_registry.json", 10),
        ("R223P_2_aesthetic_language_focus_registry.json", 15),
    ]:
        data = load_json(file_name)
        count = len(data.get("types", data.get("items", [])))
        ok = data.get("status") == "candidate_registry_only" and count >= min_count
        checks.append({"check": f"sub_registry:{file_name}", "passed": ok, "count": count})
        if not ok:
            failures.append(f"sub registry invalid: {file_name}")

    for file_name, required_terms in [
        ("R223P_2_pattern_relation_map.md", REQUIRED_PATTERNS),
        ("R223P_2_pattern_to_screen_component_evidence_mapping.md", REQUIRED_PATTERNS),
        ("R223P_2_pattern_to_unit_intensity_router_mapping.md", ["unit_phase_role", "practice_intensity", "teacher_support_density"]),
        ("R223P_2_teacher_default_vs_review_ledger_policy.md", ["teacher default view", "review ledger", "practice_pattern_type"]),
    ]:
        text = read_text(file_name)
        for term in required_terms:
            ok = term in text
            checks.append({"check": f"term:{file_name}:{term}", "passed": ok})
            if not ok:
                failures.append(f"missing {term} in {file_name}")

    all_text = "\n".join(
        p.read_text(encoding="utf-8", errors="ignore")
        for p in ROOT.iterdir()
        if p.suffix in {".md", ".json"}
    )
    for term in FORBIDDEN_TEXT:
        ok = term not in all_text
        checks.append({"check": f"forbidden:{term}", "passed": ok})
        if not ok:
            failures.append(f"forbidden term found: {term}")

    passed = all(c["passed"] for c in checks)
    result = {
        "passed": passed,
        "check_count": len(checks),
        "failed": len([c for c in checks if not c["passed"]]),
        "failures": failures,
        "decision": "PASS_CONTINUE_TO_R223P_3_SCHEMA_V0_2_DELTA" if passed else "HOLD_FOR_PATTERN_REGISTRY_HARDENING",
        "checks": checks,
    }
    (ROOT / "validate_1013R_R223P_2_pattern_registry_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps({k: result[k] for k in ["passed", "check_count", "failed", "decision"]}, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
