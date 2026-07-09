# R223P-2 模式到大单元实践强度路由映射

stage_id: 1013R_R223P_2_ART_CLASSROOM_PRACTICE_PATTERN_REGISTRY
status: candidate_mapping_only

## 路由字段

```text
unit_phase_role
lesson_position_in_unit
practice_intensity
student_work_time_ratio
teacher_support_density
performance_task_link
stage_evidence_link
```

## 映射表

| unit_phase_role | practice_intensity | 推荐模式 | 系统重点 |
| --- | --- | --- | --- |
| intro_understanding | low | observation_discovery, artwork_appreciation, comparison_judgment | 看懂、说清、建立问题 |
| appreciation_discussion | low / medium | artwork_appreciation, comparison_judgment, showcase_evaluation | 作品阅读、审美语言、观点证据 |
| technique_preparation | medium | teacher_demonstration, micro_practice, material_experiment, comparison_judgment | 示范、小练、步骤图、错误修补 |
| practice_creation | high | micro_practice, creation_progression, teacher_demonstration, showcase_evaluation | 巡视、分层支架、过程证据、时间控制 |
| showcase_evaluation | medium | showcase_evaluation, closure_transfer, comparison_judgment | 评价语言、作品说明、互评、迁移 |
| project_synthesis | high | idea_generation, material_experiment, creation_progression, showcase_evaluation | 分工、任务单、进度节点、阶段成果 |
| transfer_closure | low | closure_transfer, showcase_evaluation | 方法总结、生活迁移、后续任务 |

## 控制原则

1. 低实践强度课不应强行塞入 heavy micro_practice 或 creation_progression。
2. 高实践强度课必须强化 teacher_support_density、process_evidence 和 checkpoint。
3. 展示评价课不应只生成泛泛评价语，必须有作品说明或互评证据。
4. 技法准备课必须防止示范悬空，应接 micro_practice 或 transition_to_formal_creation。

## 当前边界

该映射只作为候选路由，不改 R223M-P5 schema v0.1。
