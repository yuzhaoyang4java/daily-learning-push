---
name: daily-learning-push
description: 每日技术学习内容生成与推送 Skill，面向后端工程师（Java/Go 等）。每天两次主动推送丰富内容：上午9点和下午14点各推送算法题（2道）+ 架构 + AI大模型 + 前沿资讯（3篇）。内容包含完整代码示例、原理图解、业务场景联想，适合中高级工程师进阶。触发场景：(1) 心跳检查时判断当前时段是否已推送；(2) 用户说"今日学习"、"给我推送内容"、"每日推送"、"学习内容"等；(3) 用户反馈内容不够详细时重新生成。
---

# Daily Learning Push

每日技术学习内容推送，**每天2次**：上午9点 + 下午14点。

**每次推送内容：**
- 🧮 **算法题 2道**（完整题库1道 + Top100热题1道）
- 🏗️ **架构专题 1篇**（原理+图解+代码+业务场景）
- 🤖 **AI大模型 1篇**（概念+实现+应用）
- 📰 **前沿资讯 3篇**（技术趋势、行业动态）

## 工作流

### Step 1：检查当前时段是否已推送

运行脚本判断幂等状态（区分早上/下午时段）：

```bash
# 上午9点检查
python3 scripts/check_push_state.py --period morning

# 下午14点检查  
python3 scripts/check_push_state.py --period afternoon
```

- 输出 `ALREADY_PUSHED`：当前时段已推送，跳过
- 输出 `NOT_PUSHED`：继续执行

### Step 2：获取今日主题

```bash
python3 scripts/get_today_topic.py --period morning   # 上午主题
python3 scripts/get_today_topic.py --period afternoon # 下午主题
```

输出 JSON，包含时段内容和序号：

**morning 示例：**
```json
{
  "period": "morning",
  "day": 4,
  "algorithm": { "index": 7, "topic": "三数之和 (LeetCode 15)", "difficulty": "Medium" },
  "algorithm_top100": { "index": 3, "topic": "两数之和 (LeetCode 1)", "difficulty": "Easy" },
  "architecture": { "index": 5, "topic": "分布式事务 Seata 原理" },
  "ai": { "index": 5, "topic": "向量数据库与 RAG 实践" },
  "tech_news": ["OpenAI GPT-5 预览", "Google Gemini 2.5 Pro 发布", "国内大模型价格战分析"]
}
```

**afternoon 示例：**
```json
{
  "period": "afternoon",
  "day": 4,
  "day_offset": 500, 
  "algorithm": { "index": 507, "topic": "二叉树最大路径和 (LeetCode 124)", "difficulty": "Hard" },
  "algorithm_top100": { "index": 23, "topic": "有效括号 (LeetCode 20)", "difficulty": "Easy" },
  "architecture": { "index": 18, "topic": "Redis Cluster 设计与实战" },
  "ai": { "index": 18, "topic": "LLM 微调策略全解析" },
  "tech_news": ["阿里巴巴通义千问 Qwen3 官宣", "GitHub Copilot 免费版上线", "Cursor 0.50 AI IDE 评测"]
}
```

### Step 3：生成详细内容

读取 `references/content-template.md` 获取格式规范，按模板生成各方向内容。

**内容质量标准（必须满足）：**

| 类型 | 要求 |
|------|------|
| 🧮 **算法题×2** | 题目描述 + 暴力解→优化解演进 + 完整代码 + 复杂度分析 |
| 🏗️ **架构专题** | 原理详解 + ASCII 架构图 + 代码示例 + 业务场景 |
| 🤖 **AI 专题** | 概念 + 流程图 + 实现要点 + 应用案例 |
| 📰 **前沿资讯×3** | 标题 + 一句话总结 + 来源链接（可选） |

详细格式规范见 `references/content-template.md`。
主题库见 `references/algorithm-topics.md`、`references/top100-topics.md`、`references/architecture-topics.md`、`references/ai-topics.md`。

### Step 4：保存 + 写入 Redoc + 推送

1. 将内容写入 `memory/YYYY-MM-DD-{morning|afternoon}.md`（时段文件）
2. 追加到 `memory/YYYY-MM-DD.md`（当天汇总）
3. **写入 Redoc 学习空间子文档**：

```bash
# 创建当次推送的 Redoc 文档
REDOC_SKILL=/app/skills/hi-redoc-curd
bash "$REDOC_SKILL/scripts/hi-redoc-curd.sh" \
  -p memory/YYYY-MM-DD-{morning|afternoon}.md
# 保存返回的 shortcutId 到 push-state.json
```

4. **更新学习空间索引文档**（父文档 ID: `86149ebd485f8a447b3760acfc5f4710`）：
   - 在索引表格中追加新一行：日期 · 时段 · 内容摘要 · 新文档链接
   - 保持历史记录完整，按日期倒序排列

```bash
# 更新学习空间父文档（追加新行到归档表格）
bash "$REDOC_SKILL/scripts/hi-redoc-curd.sh" \
  -u 86149ebd485f8a447b3760acfc5f4710 \
  -c "（完整更新后的学习空间文档内容）"
```

5. 更新推送状态：

```bash
python3 scripts/update_push_state.py --period morning    # 上午
python3 scripts/update_push_state.py --period afternoon  # 下午
```

6. 在当前会话展示内容，并回复 Redoc 链接给用户

## Redoc 配置

- **学习空间父文档**: `https://docs.xiaohongshu.com/doc/86149ebd485f8a447b3760acfc5f4710`
- **父文档 shortcutId**: `86149ebd485f8a447b3760acfc5f4710`
- 每次推送创建一个子文档，并更新父文档的归档索引表格
- push-state.json 中新增 `redocHistory` 记录每次推送的 shortcutId

## 推送时段配置

推送状态保存在 `memory/push-state.json`，结构：

```json
{
  "lastMorningPush": "2026-03-27",
  "lastAfternoonPush": "2026-03-27",
  "dailyProgress": { "morning": { ... }, "afternoon": { ... } }
}
```

## 用户配置

安装后在工作区 `MEMORY.md` 中添加以下配置（可选，使用默认值）：

```markdown
## 每日学习推送配置
- 技术方向：Java 后端（默认）
- 当前水平：中级（默认）
- 业务背景：电商/社交（默认）
- 推送时间：上午9点 + 下午14点
```
