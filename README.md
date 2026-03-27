# 📚 Daily Learning Push

> 每日技术学习内容自动推送 Skill，面向后端工程师（Java/Go 等）。  
> 接入 OpenClaw 后，每天 9:00 和 14:00 自动推送高质量学习内容。

---

## ✨ 功能概览

**每天 2 次自动推送**，每次推送包含：

| 类型 | 数量 | 内容说明 |
|------|------|----------|
| 🧮 算法-完整题库 | 1 道 | 暴力解→最优解演进 + 完整代码 + 复杂度分析 |
| 🧮 算法-热题100 | 1 道 | LeetCode 高频面试题，附完整链接 |
| 🏗️ 系统架构 | 1 篇 | 原理详解 + ASCII 架构图 + 实战代码 + 业务场景 |
| 🤖 AI 大模型 | 1 篇 | 概念 + 流程图 + 工程实现 + 应用案例 |
| 📰 前沿资讯 | 3 篇 | 技术动态 + 来源链接 + 影响分析 |

**推送时段：**
```
上午 9:00  ±5 分钟  →  算法 + 架构 + AI + 资讯
下午 14:00 ±5 分钟  →  算法 + 架构 + AI + 资讯（不同主题）
```

**内容归档：**
- 📁 本地保存：`memory/YYYY-MM-DD-morning.md` / `-afternoon.md`
- ☁️ Redoc 云端：每次推送自动写入你的学习空间，永久备份

---

## 🚀 快速开始

### 第一步：安装 Skill

将本仓库克隆到 OpenClaw workspace 的 skills 目录：

```bash
cd ~/.openclaw/workspace/skills
git clone https://github.com/yuzhaoyang4java/daily-learning-push.git
```

或公司内网 GitLab：

```bash
cd ~/.openclaw/workspace/skills
git clone git@code.devops.xiaohongshu.com:zhaoyangyu/ai-daily-learning-push.git daily-learning-push
```

### 第二步：一键初始化

运行初始化脚本，自动完成以下配置：
- 为你创建专属的 Redoc 学习空间父文档
- 生成个人推送配置文件
- 初始化学习进度（从 Day 1 开始）

```bash
cd ~/.openclaw/workspace/skills/daily-learning-push
python3 scripts/init_user.py
```

> ⚠️ **注意**：每位用户独立运行，各自拥有独立的 Redoc 学习空间，互不干扰。

### 第三步：配置心跳

将 HEARTBEAT.md 中的内容复制到工作区：

```bash
# 如果 HEARTBEAT.md 不存在，直接复制
cp ~/.openclaw/workspace/skills/daily-learning-push/HEARTBEAT.md \
   ~/.openclaw/workspace/HEARTBEAT.md

# 如果已存在，追加以下内容：
cat ~/.openclaw/workspace/skills/daily-learning-push/HEARTBEAT.md \
   >> ~/.openclaw/workspace/HEARTBEAT.md
```

### 第四步：验证配置

```bash
cd ~/.openclaw/workspace/skills/daily-learning-push

# 检查推送状态
python3 scripts/check_push_state.py --period morning
python3 scripts/check_push_state.py --period afternoon

# 检查心跳窗口检测
bash scripts/heartbeat_check.sh
```

---

## 📋 使用方式

### 自动推送

配置完成后，OpenClaw 会在每次心跳时检测时段，自动在 9:00 和 14:00 推送内容，**无需任何手动操作**。

### 手动触发

对 OpenClaw 说以下任意一句话即可立即触发推送：

```
今日学习
给我推送内容
每日推送
学习内容
```

### 查看学习空间

初始化后，你的 Redoc 学习空间 URL 保存在：

```bash
cat ~/.openclaw/workspace/memory/.redoc-config.json
# 输出：{ "parentDocUrl": "https://docs.xiaohongshu.com/doc/xxxx", ... }
```

---

## 📁 项目结构

```
daily-learning-push/
├── SKILL.md                      # Skill 核心定义（OpenClaw 读取）
├── HEARTBEAT.md                  # 心跳推送配置（复制到 workspace）
├── README.md                     # 使用说明（本文件）
│
├── scripts/                      # 核心脚本
│   ├── init_user.py              # ⭐ 新用户初始化（创建 Redoc 学习空间）
│   ├── check_push_state.py       # 检查当前时段是否已推送
│   ├── get_today_topic.py        # 获取今日各时段主题
│   ├── update_push_state.py      # 更新推送状态
│   ├── heartbeat_check.sh        # 心跳时段窗口检测
│   ├── auto_switch_heartbeat.sh  # 自动调节心跳频率
│   ├── get_redoc_config.py       # 读取个人 Redoc 配置
│   └── sync_to_remotes.py        # 同步代码到远程仓库
│
└── references/                   # 主题库与模板
    ├── content-template.md       # 内容格式规范
    ├── algorithm-topics.md       # 算法题库（69 题，含 LeetCode 链接）
    ├── top100-topics.md          # LeetCode 热题 100（全链接版）
    ├── architecture-topics.md    # 架构设计主题库（200+ 主题）
    ├── ai-topics.md              # AI 大模型主题库（200+ 主题）
    ├── algorithm-roadmap.md      # 算法学习路线
    ├── architecture-roadmap.md   # 架构学习路线
    ├── ai-roadmap.md             # AI 学习路线
    └── tech-news-template.md     # 前沿资讯模板
```

> **注意**：`memory/` 目录为本地个人数据（已 .gitignore），不上传到 Git 仓库。  
> 详见下方「数据存储架构」说明。

---

## 🔧 手动脚本操作

```bash
SKILL=~/.openclaw/workspace/skills/daily-learning-push

# 1. 初始化（首次使用）
python3 $SKILL/scripts/init_user.py

# 2. 检查今天状态
python3 $SKILL/scripts/check_push_state.py --period morning
python3 $SKILL/scripts/check_push_state.py --period afternoon

# 3. 获取今日主题（不执行推送）
python3 $SKILL/scripts/get_today_topic.py --period morning
python3 $SKILL/scripts/get_today_topic.py --period afternoon

# 4. 心跳窗口检测（判断当前是否应推送）
bash $SKILL/scripts/heartbeat_check.sh
# 返回：SHOULD_PUSH_MORNING / SHOULD_PUSH_AFTERNOON / WAIT_NEXT_PERIOD / ALREADY_PUSHED_*

# 5. 手动更新推送状态（推送后执行）
python3 $SKILL/scripts/update_push_state.py --period morning
python3 $SKILL/scripts/update_push_state.py --period afternoon

# 6. 查看个人 Redoc 配置
python3 $SKILL/scripts/get_redoc_config.py
```

---

## 🗄️ 数据存储架构

本项目采用**代码与数据分离**设计：

| 位置 | 内容 | 同步方式 | 说明 |
|------|------|----------|------|
| `scripts/` `references/` | 脚本和主题库 | ✅ Git 仓库同步 | 公共代码，可多人复用 |
| `~/.openclaw/workspace/memory/` | 推送状态和学习记录 | ❌ 本地保存 | 个人数据，不上传 |
| Redoc 学习空间 | 推送内容归档 | ☁️ 云端存储 | 永久备份，跨设备访问 |

**个人数据文件说明：**

```
~/.openclaw/workspace/memory/
├── .redoc-config.json          # 你的 Redoc 学习空间配置（init_user.py 自动创建）
├── push-state.json             # 推送进度（Day N，各方向索引）
├── 2026-03-27-morning.md       # 上午推送内容本地副本
├── 2026-03-27-afternoon.md     # 下午推送内容本地副本
└── 2026-03-27.md               # 当天会话笔记
```

---

## ⚙️ 自动化说明

### 心跳频率自适应

```
工作日 08:00-18:00  →  15 分钟心跳（高频，精准捕捉推送窗口）
其他时间            →  1 小时心跳（低频，节省资源）
```

### 推送幂等性

每个时段只推送一次，重复触发会自动跳过：

| 检测结果 | 含义 |
|----------|------|
| `SHOULD_PUSH_MORNING` | 应推送上午内容 |
| `SHOULD_PUSH_AFTERNOON` | 应推送下午内容 |
| `ALREADY_PUSHED_MORNING` | 今天上午已推送，跳过 |
| `ALREADY_PUSHED_AFTERNOON` | 今天下午已推送，跳过 |
| `WAIT_NEXT_PERIOD` | 非推送窗口，等待下一时段 |

### 学习进度持续递增

每次推送后自动递增各方向索引（Day 1 → Day 2 → ...），确保每天内容不重复：

- 上午：算法索引 0, 1, 2...
- 下午：算法索引 500, 501, 502...（+500 偏移避免重复）

---

## 📚 主题库

| 主题库 | 文件 | 数量 |
|--------|------|------|
| 算法-完整题库 | [algorithm-topics.md](references/algorithm-topics.md) | 69 题（含 LeetCode 链接） |
| 算法-热题100 | [top100-topics.md](references/top100-topics.md) | 100 题（面试必刷） |
| 架构设计 | [architecture-topics.md](references/architecture-topics.md) | 200+ 主题 |
| AI 大模型 | [ai-topics.md](references/ai-topics.md) | 200+ 主题 |
| 前沿资讯 | [tech-news-template.md](references/tech-news-template.md) | 动态生成 |

LeetCode 热题 100 学习计划：https://leetcode.cn/studyplan/top-100-liked/

---

## 🗓️ 学习路线

- 📈 [算法学习路线](references/algorithm-roadmap.md)
- 🏛️ [架构学习路线](references/architecture-roadmap.md)
- 🧠 [AI 学习路线](references/ai-roadmap.md)

---

## 📝 更新日志

- **v2.0** (2026-03-27): 新用户一键初始化 + 移除所有硬编码个人数据
- **v1.0** (2026-03-27): 双时段推送（9:00 + 14:00），Redoc 归档集成

---

## 🤝 贡献

欢迎 PR 补充：
- 新的算法题（附 LeetCode 链接）
- 架构设计主题与实战案例
- AI 应用场景与工程实践
- 前沿技术资讯来源

---

## 📄 License

MIT License - 详见 [LICENSE](LICENSE)
