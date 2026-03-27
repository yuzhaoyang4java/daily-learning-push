---
name: daily-learning-push
description: 每日技术学习内容生成与推送 Skill，面向后端工程师（Java/Go 等）。每天主动推送三个方向的详细学习内容：算法题（LeetCode）、系统架构、AI大模型。内容包含完整代码示例、原理图解、业务场景联想，适合中高级工程师进阶。触发场景：(1) 心跳检查时判断今日未推送则自动生成；(2) 用户说"今日学习"、"给我推送内容"、"每日推送"、"学习内容"等；(3) 用户反馈内容不够详细时重新生成。
---

# Daily Learning Push

每日技术学习内容推送，三方向并行：算法 + 架构 + AI大模型。

## 工作流

### Step 1：检查今日是否已推送

运行脚本判断幂等状态：

```bash
python3 scripts/check_push_state.py
```

- 输出 `ALREADY_PUSHED`：今日已推送，跳过（回复用户已推送并展示内容路径）
- 输出 `NOT_PUSHED`：继续执行

### Step 2：获取今日主题

```bash
python3 scripts/get_today_topic.py
```

输出 JSON，包含今日三个方向的主题和序号：

```json
{
  "day": 4,
  "algorithm": { "index": 3, "topic": "最长回文子串", "leetcode": 5, "difficulty": "Medium" },
  "architecture": { "index": 3, "topic": "消息队列原理与实战" },
  "ai": { "index": 3, "topic": "Prompt Engineering 进阶" }
}
```

### Step 3：生成详细内容

读取 `references/content-template.md` 获取格式规范，按模板生成三方向内容。

**内容质量标准（必须满足）：**

- 🧮 **算法**：题目描述 + 暴力解 → 优化解演进 + 至少 2 种解法完整代码 + 复杂度分析 + 变种题 + 面试追问
- 🏗️ **架构**：原理详解 + ASCII 架构图 + 关键代码示例 + 对比表格 + 小红书/电商业务场景联想 + 面试高频问题
- 🤖 **AI**：概念解释 + 完整流程图 + 工程实现要点 + 业务场景应用 + 效果评估方法

详细格式规范见 `references/content-template.md`。
主题库见 `references/algorithm-topics.md`、`references/architecture-topics.md`、`references/ai-topics.md`。

### Step 4：保存与推送

1. 将内容写入 `memory/YYYY-MM-DD.md`（覆盖当天文件）
2. 更新推送状态：

```bash
python3 scripts/update_push_state.py
```

3. 直接在当前会话中展示内容给用户

## 用户配置

安装后在工作区 `MEMORY.md` 中添加以下配置（可选，不配置则使用默认值）：

```markdown
## 每日学习推送配置
- 技术方向：Java 后端（默认）
- 当前水平：中级（默认）
- 业务背景：电商/社交（默认）
- 推送时间：每天上午（心跳触发）
```

## 状态文件

推送状态保存在 `memory/push-state.json`，结构见 `references/content-template.md`。
