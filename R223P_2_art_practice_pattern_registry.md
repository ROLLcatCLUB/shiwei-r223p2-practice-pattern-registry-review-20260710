# R223P-2 小学美术课堂实践模式候选注册表

stage_id: 1013R_R223P_2_ART_CLASSROOM_PRACTICE_PATTERN_REGISTRY
status: candidate_registry_only
schema_v0_2_published: false
formal_ui: false

## 定位

本注册表把 R223P-1 研究接收包中的 10 类美术课堂实践模式，整理成候选 registry。

它不是组件库，不是 UI，也不是 classroom_event_schema v0.2 发布。它的作用是为 R223P-3 schema delta 和 R223P-4 三样本回归提供稳定的模式主键。

## 三层边界

```text
general_pedagogy_core = 通用教学推理底座
art_subject_adapter = 美术学科实践模式适配层
unit_lesson_practice_intensity_router = 大单元—课时实践强度路由
```

本文件中的 10 个模式均属于：

```text
layer = art_subject_adapter
```

## 10 类候选模式

| pattern_id | 中文名 | 核心功能 | 解决的学生问题 | 典型位置 |
| --- | --- | --- | --- | --- |
| observation_discovery | 观察发现 | 先看见关键特征 | 只说好看、像不像，缺少依据 | 导入、创作前、赏析前 |
| comparison_judgment | 对比判断 | 建立差异和判断标准 | 只凭感觉判断，不能说理由 | 观察后、示范前、中途调控 |
| artwork_appreciation | 作品赏析 | 打开思路、建立美术语言 | 不会看作品、不会借鉴 | 导入、构思前、评价前 |
| teacher_demonstration | 教师示范 | 让关键动作直观化 | 知道目标但不会操作 | 技法突破处、创作前 |
| micro_practice | 前置小练习 | 低风险试错并迁移到正式作品 | 不敢下手或技法未过关 | 示范后、正式创作前 |
| material_experiment | 材料实验 | 通过试材理解材料特性 | 材料选择随意或技法失败 | 材料选择前、项目中段 |
| idea_generation | 构思生成 | 把想法外显成方案 | 想不出、作品雷同 | 正式创作前 |
| creation_progression | 创作推进 | 控制创作节奏和中途调控 | 中途停滞、偏题、进度差异大 | 正式创作中段 |
| showcase_evaluation | 展示评价 | 把作品和表达转成评价证据 | 会做不会说，评价空泛 | 收尾、二改前 |
| closure_transfer | 收束迁移 | 把方法带到生活或后续任务 | 做完即结束，不能迁移 | 结课、单元阶段收束 |

## 模式与组件的关系

```text
课堂实践模式 = 教学展开依据
组件 = 实现某个模式时可调用的课堂动作或 surface
大屏 / 学习单 / 证据 = 模式触发后的派生物
```

例如：

```text
comparison_judgment
→ 可调用 compare_two_images
→ 大屏显示双图对比
→ 学习单记录 difference_and_reason
→ 评价学生能否给出判断依据
```

## 默认教师稿与 review ledger 分层

默认教师稿只应出现自然教学语言，例如：

```text
教师出示两张作品，请学生说一说哪一处边缘更有版画味。
```

review ledger 才记录：

```text
practice_pattern_type = comparison_judgment
component_trigger = compare_two_images
learning_sheet_fields = difference_and_reason
```

## 当前禁止

```text
不改 R223M-P5 schema v0.1
不发布 v0.2
不改 R222D 组件库
不改 R223M/N/O 已有教师稿
不做 UI
不接 runtime/model/prompt/db
不 formal apply
```
