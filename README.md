# Daily Learning Push

每日技术学习内容推送 Skill，面向后端工程师（Java/Go 等）。

## 🎯 功能

**每天 2 次** 主动推送丰富技术内容：

| 时段 | 时间 | 推送内容 |
|------|------|----------|
| 🌅 **上午** | 9:00 | 算法2道 + 架构1篇 + AI 1篇 + 资讯3篇 |
| 🌇 **下午** | 14:00 | 算法2道 + 架构1篇 + AI 1篇 + 资讯3篇 |

### 每次推送详情

- 🧮 **算法题 2道**
  - 完整题库 1道（覆盖 LeetCode 2000+ 题）
  - LeetCode 热题 100 精选 1道（面试高频）
- 🏗️ **系统架构 1篇** — 分布式原理 + 架构图 + 实战代码 + 业务场景
- 🤖 **AI 大模型 1篇** — 概念解析 + 流程图 + 工程实现 + 应用案例
- 📰 **前沿资讯 3篇** — 最新技术动态、行业趋势、产品发布

## 📦 项目结构

```
daily-learning-push/
├── SKILL.md                    # Skill 定义文件
├── README.md                   # 项目说明
├── HEARTBEAT.md                # 心跳推送配置指南
├── scripts/                    # 核心脚本
│   ├── check_push_state.py     # 检查时段是否已推送
│   ├── get_today_topic.py      # 获取各时段主题
│   ├── update_push_state.py    # 更新推送状态
│   └── heartbeat_check.sh      # 心跳时段检测脚本
└── references/                 # 主题库与模板
    ├── content-template.md     # 内容格式规范
    ├── algorithm-topics.md     # 算法题库（完整+链接）
    ├── top100-topics.md        # LeetCode 热题100（完整链接版）
    ├── architecture-topics.md  # 架构主题库
    ├── ai-topics.md            # AI 主题库
    ├── algorithm-roadmap.md    # 算法学习路线
    ├── architecture-roadmap.md # 架构学习路线
    ├── ai-roadmap.md           # AI 学习路线
    └── tech-news-template.md   # 前沿资讯模板

# 本地运行时生成（已排除在 GitHub 同步外）
~/.openclaw/workspace/memory/   # OpenClaw 工作区 memory 目录
├── push-state.json             # 个人推送进度和索引状态
├── 2026-03-27-morning.md       # 每日上午推送内容
├── 2026-03-27-afternoon.md     # 每日下午推送内容
└── 2026-03-27.md               # 当天内容汇总
```

### 数据存储架构说明

本项目采用**代码与数据分离**的设计：

| 位置 | 内容 | 同步策略 | 用途 |
|------|------|----------|------|
| `scripts/` `references/` | 脚本和主题库 | ✅ GitHub 同步 | **公共代码**，可多人复用 |
| `memory/` | 推送状态和学习记录 | ❌ 本地保存 | **个人数据**，时序敏感 |
| **Redoc** | 归档文档 | ☁️ 云端存储 | **永久备份**，跨设备访问 |

**为何 `memory/` 不提交到 GitHub？**

1. **个人化** — `push-state.json` 记录的是你的推送进度（如 Day 8），若同步给他人会混淆
2. **时序敏感** — 每天索引递增，不同用户使用进度不同
3. **可重建** — 即使丢失也不影响功能，下次推送会重新创建
4. **隐私** — 学习记录属于个人使用痕迹

**如何备份个人记录？**

```bash
# 方案1：本地备份
cp -r ~/.openclaw/workspace/memory ~/Documents/backup/

# 方案2：Redoc 归档（推荐）
# 每次推送自动写入 Redoc 云端，历史内容永不丢失
```

## 🚀 使用方式

### OpenClaw 环境

1. 将本文件夹复制到 OpenClaw workspace skills 目录：
   ```bash
   cp -r daily-learning-push ~/.openclaw/workspace/skills/
   ```

2. 配置 `HEARTBEAT.md`（参考本目录下的 HEARTBEAT.md）

3. 或在 `.openclaw/workspace` 目录下创建 `HEARTBEAT.md` 并引用：
   ```bash
   # 复制示例配置
   cp ~/.openclaw/workspace/skills/daily-learning-push/HEARTBEAT.md \
      ~/.openclaw/workspace/HEARTBEAT.md
   ```

### 手动触发验证

```bash
cd ~/.openclaw/workspace/skills/daily-learning-push

# 检查时段状态
python3 scripts/check_push_state.py --period morning
python3 scripts/check_push_state.py --period afternoon

# 获取今日主题
python3 scripts/get_today_topic.py --period morning    # 上午主题
python3 scripts/get_today_topic.py --period afternoon  # 下午主题（索引+500）

# 心跳时段检测
bash scripts/heartbeat_check.sh

# 推送后更新状态
python3 scripts/update_push_state.py --period morning
python3 scripts/update_push_state.py --period afternoon
```

## 📋 内容质量标准

| 方向 | 要求 |
|------|------|
| 🧮 算法-完整题库 | 题目描述 + 暴力→优化解演进 + 完整代码 + 复杂度分析 + 变种题 |
| 🧮 算法-Top100 | LeetCode 热题精选，最优解详解，面试重点标注 |
| 🏗️ 架构 | 原理详解 + ASCII 架构图 + 完整 Java/Go 代码 + 业务场景 + 面试高频问题 |
| 🤖 AI | 概念解释 + 完整流程图 + 工程实现要点 + 业务场景应用 |
| 📰 资讯 | 标题 + 一句话总结（3篇最新最热技术动态） |

## ⏰ 自动化配置

### 推送时段

```
9:00  ± 5分钟   → 上午推送
copy14:00 ± 5分钟   → 下午推送
```

### 心跳频率

```bash
# 通过 auto_switch_heartbeat.sh 自动调节
bash scripts/auto_switch_heartbeat.sh

# 工作日 08:00-18:00 → 15分钟心跳（高频检测）
# 其他时间 → 1小时心跳（低频节能）
```

### 状态文件

```json
{
  "lastMorningPush": "2026-03-27",
  "lastAfternoonPush": "2026-03-27",
  "totalDays": 7,
  "totalPushes": 14,
  "nextIndex": {
    "algorithm": 9,
    "algorithm_top100": 5,
    "architecture": 10,
    "ai": 10,
    "technews": 3
  }
}
```

## 📚 主题库

| 主题库 | 链接 | 数量 |
|--------|------|------|
| 算法-完整题库 | [algorithm-topics.md](/references/algorithm-topics.md) | 69+ 题（带链接） |
| 算法-热题100 | [top100-topics.md](/references/top100-topics.md) | 100 题（面试必刷，完整链接） |
| 架构设计 | [architecture-topics.md](/references/architecture-topics.md) | 200+ 主题 |
| AI 大模型 | [ai-topics.md](/references/ai-topics.md) | 200+ 主题 |
| 前沿资讯 | [tech-news-template.md](/references/tech-news-template.md) | 动态生成 |

### 快速访问 LeetCode

所有算法题均附带完整链接，格式：`https://leetcode.cn/problems/{slug}/`

热题 100 学习计划页面：https://leetcode.cn/studyplan/top-100-liked/

## 🗓️ 学习路线

- 📈 [算法学习路线](/references/algorithm-roadmap.md)
- 🏛️ [架构学习路线](/references/architecture-roadmap.md)
- 🧠 [AI 学习路线](/references/ai-roadmap.md)

## 📝 近期更新

- **v4.3** (2026-03-27): 双时段推送调试验证，heartbeat 配置完善
- **v4.2** (2026-03-27): 调整为每天2次推送（9:00 + 14:00）
- **v4.1** (2026-03-27): 添加完整 LeetCode 题目链接
- **v4.0** (2026-03-27): 新增 5 方向内容（算法/架构/AI/资讯/推荐）

## 🤝 贡献

欢迎提交 PR 补充：
- 新的算法题（附带 LeetCode 链接）
- 架构设计主题与实战案例
- AI 应用场景与工程实践
- 前沿技术资讯来源
- 代码优化与文档改进

## 📄 License

MIT License - 详见 [LICENSE](LICENSE)
