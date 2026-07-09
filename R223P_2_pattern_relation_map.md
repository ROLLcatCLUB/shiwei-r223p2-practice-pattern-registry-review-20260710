# R223P-2 实践模式关系图

stage_id: 1013R_R223P_2_ART_CLASSROOM_PRACTICE_PATTERN_REGISTRY
status: candidate_relation_map_only

## 基本关系

```text
观察发现
→ 对比判断 / 作品赏析
→ 教师示范 / 前置小练习 / 材料实验 / 构思生成
→ 创作推进
→ 展示评价
→ 收束迁移
```

这不是固定流程，而是可插入、可回退、可跳过的事件簇。

## 高频组合

| 组合 | 适用场景 | 说明 |
| --- | --- | --- |
| observation_discovery → comparison_judgment | 学生先看见，再分辨 | 适合色彩、材料、构图、设计判断 |
| artwork_appreciation → idea_generation | 先赏析，再构思 | 防止学生想不出或只照抄 |
| teacher_demonstration → micro_practice | 先示范，再短练 | 防止示范悬空 |
| material_experiment → micro_practice → creation_progression | 先试材，再试做，再正式推进 | 适合材料技法和综合材料 |
| creation_progression → comparison_judgment → creation_progression | 中途投屏对比后回到创作 | 适合二改和过程调控 |
| showcase_evaluation → closure_transfer | 展示后把方法迁移到单元或生活 | 防止做完即结束 |

## 回退关系

| 当前事件 | 触发问题 | 回退模式 |
| --- | --- | --- |
| creation_progression | 大量学生不会操作 | teacher_demonstration |
| creation_progression | 作品方向偏离任务 | comparison_judgment |
| creation_progression | 材料失败 | material_experiment |
| idea_generation | 想法空泛 | artwork_appreciation |
| showcase_evaluation | 评价空泛 | artwork_appreciation / comparison_judgment |

## 与组件的关系

模式不是组件。组件只是某个模式下可调用的课堂动作或 surface。

```text
practice_pattern_type = comparison_judgment
component_candidate = compare_two_images
```

```text
practice_pattern_type = teacher_demonstration
component_candidate = technique_step_demo
```

## 与 schema v0.2 的关系

本关系图不发布 v0.2，只为 R223P-3 delta 提供候选依据。
