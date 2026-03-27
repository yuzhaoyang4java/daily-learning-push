# Daily Learning Push

每日技术学习内容推送 Skill，面向后端工程师（Java/Go 等）。

## 🎯 功能

每天主动推送三个方向的详细学习内容：
- 🧮 **算法题**（LeetCode）：经典题目 + 多解法 + 复杂度分析
- 🏗️ **系统架构**：分布式系统原理 + 实战代码
- 🤖 **AI 大模型**：Prompt Engineering + 业务应用

## 📦 项目结构

```
daily-learning-push/
├── SKILL.md                    # Skill 定义文件
├── README.md                   # 项目说明
├── scripts/                    # 核心脚本
│   ├── check_push_state.py     # 检查今日是否已推送
│   ├── get_today_topic.py      # 获取今日三方向主题
│   ├── update_push_state.py    # 更新推送状态
│   └── heartbeat_check.sh      # 心跳检查脚本
└── references/                 # 参考数据
    ├── content-template.md     # 内容格式规范
    ├── algorithm-topics.md     # 算法题目库
    ├── architecture-topics.md  # 架构主题库
    └── ai-topics.md            # AI 主题库
```

## 🚀 使用方式

### OpenClaw 环境

1. 将本文件夹复制到 OpenClaw workspace skills 目录：
   ```bash
   cp -r daily-learning-push ~/.openclaw/workspace/skills/
   ```

2. 在 `HEARTBEAT.md` 中添加调用逻辑（参考 SKILL.md）

3. 或使用手动触发：
   ```bash
   cd ~/.openclaw/workspace/skills/daily-learning-push
   python3 scripts/check_push_state.py
   ```

### 独立使用

```bash
# 检查今日状态
python3 scripts/check_push_state.py

# 获取今日主题
python3 scripts/get_today_topic.py

# 更新状态（推送后执行）
python3 scripts/update_push_state.py
```

## 📋 内容质量标准

| 方向 | 要求 |
|------|------|
| 🧮 算法 | ≥2 种解法完整代码 + 复杂度分析 + 变种题 + 面试追问 |
| 🏗️ 架构 | ASCII 架构图 + 完整 Java 代码 + 业务场景 + 面试高频问题 |
| 🤖 AI | 完整流程图 + 工程实现要点 + 业务场景应用 + 评估指标 |

## 🔄 自动化支持

- **OpenClaw 心跳**：自动检测时间并推送
- **分时段策略**：工作日 15m / 夜间周末 1h

## 📝 主题库

- 算法：[LeetCode 经典题](/references/algorithm-topics.md)
- 架构：[分布式系统](/references/architecture-topics.md)
- AI：[大模型应用](/references/ai-topics.md)

## 🤝 贡献

欢迎提交 PR 补充：
- 新的算法题
- 架构主题
- AI 应用场景
- 代码优化

## 📄 License

MIT License - 详见 [LICENSE](LICENSE)
