# R223P-2 教师默认稿与 Review Ledger 分层策略

stage_id: 1013R_R223P_2_ART_CLASSROOM_PRACTICE_PATTERN_REGISTRY
status: policy_candidate_only

## 基本原则

```text
教师默认稿 = 成熟教案文稿
review ledger = 结构化事件、模式、组件、大屏、学习单、证据、来源和规则
```

实践模式、示范类型、小练类型、赏析支架类型和美术语言枚举，不应直接以字段名形式进入教师默认稿。

## 默认教师稿可见

默认教师稿可以自然表达：

```text
教师出示两张作品，请学生比较哪一处边缘更有版画味。
学生先试调一小块颜色，再把这块颜色用于自己的画面。
教师巡视时重点看学生是否能说出材料选择理由。
```

默认教师稿不应出现：

```text
practice_pattern_type = comparison_judgment
micro_practice_type = color_mix
component_trigger = compare_two_images
```

## Review Ledger 记录

review ledger 应记录：

```text
practice_pattern_type
demonstration_type
micro_practice_type
appreciation_scaffold_type
aesthetic_language_focus
screen_trigger_candidates
component_trigger_candidates
learning_sheet_fields
evidence_outputs
unit_phase_role
practice_intensity
source_basis
```

## 模式级显示策略

| 内容 | teacher default view | review ledger |
| --- | --- | --- |
| pattern_id | hidden | visible |
| cn_label | optional as natural heading | visible |
| student_problem_solved | naturalized | visible |
| screen/component triggers | short note only if needed | full |
| learning_sheet_fields | naturalized | full |
| evidence_outputs | visible as teaching evidence | full |
| misuse_risks | hidden unless high risk | full |
| source_basis | hidden | full |

## 边界

本策略不改现有教师稿，只作为后续 R223P-3 / R223P-4 的候选显示规则。
