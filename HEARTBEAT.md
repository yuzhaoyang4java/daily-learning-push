# HEARTBEAT.md - 智能心跳策略 + 双时段推送

> **重要：每天2次自动推送**
> - 上午9:00：morning 时段推送
> - 下午14:00：afternoon 时段推送

每次推送内容：算法2道 + 架构1篇 + AI 1篇 + 资讯3篇

---

## 执行流程

**每次收到心跳时，按以下顺序执行：**

### Step 1: 时间检测与心跳频率切换
```bash
bash ~/.openclaw/scripts/auto_switch_heartbeat.sh
```
- 工作日 08:00-18:00 → 15分钟心跳（高频）
- 其他时间 → 1小时心跳（低频）

---

### Step 2: 智能推送时段检测

运行心跳检查脚本，它会判断当前是否在推送窗口：

```bash
bash ~/.openclaw/workspace/skills/daily-learning-push/scripts/heartbeat_check.sh
```

**输出结果判断：**

| 输出 | 含义 | 操作 |
|------|------|------|
| `SHOULD_PUSH_MORNING` | 上午 9:00 需要推送 | ✅ 执行 morning 推送 |
| `SHOULD_PUSH_AFTERNOON` | 下午 14:00 需要推送 | ✅ 执行 afternoon 推送 |
| `ALREADY_PUSHED_MORNING` | 上午已推送 | ⏭️ 跳过，等待下午 |
| `ALREADY_PUSHED_AFTERNOON` | 下午已推送 | ⏭️ 跳过，等待明天 |
| `SKIP_TOO_EARLY` | 时间未到 9:00 | ⏭️ 跳过 |
| `WAIT_NEXT_PERIOD` | 非推送窗口期间 | ⏭️ 跳过 |

**推送窗口：** 目标时间前后各5分钟（8:55-9:05 / 13:55-14:05）

---

### Step 3: 执行推送

#### 如果是 `SHOULD_PUSH_MORNING`

```bash
# 1. 获取主题（上午索引）
python3 ~/.openclaw/workspace/skills/daily-learning-push/scripts/get_today_topic.py --period morning | tee /tmp/morning_topics.json

# 2. 读取 content-template.md 格式规范
# 3. 生成详细内容（算法+架构+AI+资讯）
# 4. 保存到 memory/YYYY-MM-DD-morning.md
# 5. 推送内容给用户
# 6. 更新状态

python3 ~/.openclaw/workspace/skills/daily-learning-push/scripts/update_push_state.py --period morning

# 确认更新成功，输出状态
python3 ~/.openclaw/workspace/skills/daily-learning-push/scripts/check_push_state.py --period morning
```

#### 如果是 `SHOULD_PUSH_AFTERNOON`

```bash
# 1. 获取主题（下午索引，+500偏移避免重复）
python3 ~/.openclaw/workspace/skills/daily-learning-push/scripts/get_today_topic.py --period afternoon | tee /tmp/afternoon_topics.json

# 2. 读取 content-template.md 格式规范
# 3. 生成详细内容（算法+架构+AI+资讯）
# 4. 保存到 memory/YYYY-MM-DD-afternoon.md
# 5. 推送内容给用户
# 6. 更新状态

python3 ~/.openclaw/workspace/skills/daily-learning-push/scripts/update_push_state.py --period afternoon

# 确认更新成功，输出状态
python3 ~/.openclaw/workspace/skills/daily-learning-push/scripts/check_push_state.py --period afternoon
```

---

## 内容质量标准

每时段必须包含：

| 类型 | 数量 | 质量要求 |
|------|------|----------|
| 🧮 **算法-完整题库** | 1道 | 暴力→优解演进 + 完整代码 + 复杂度分析 |
| 🧮 **算法-Top100热题** | 1道 | 最优解详解，面试重点标注 |
| 🏗️ **架构设计** | 1篇 | 原理 + ASCII图 + 代码 + 业务场景 |
| 🤖 **AI大模型** | 1篇 | 概念 + 流程图 + 工程实现 + 案例 |
| 📰 **前沿资讯** | 3篇 | 标题 + 一句话总结（无需详细展开） |

---

## 强制约定

⚠️ **绝不偷懒！**

1. **9:00-9:05 心跳** → 必须检测并执行 morning 推送
2. **14:00-14:05 心跳** → 必须检测并执行 afternoon 推送（不管上午是否推送过）
3. **任何时段输出 `SHOULD_PUSH_*`** → 必须立即执行推送并更新状态
4. **不得以任何理由跳过推送**（内容太长、格式复杂都不成立）

---

## 验证当前状态

运行以下命令自查：

```bash
# 检查推送状态
echo "=== Morning ===" && python3 ~/.openclaw/workspace/skills/daily-learning-push/scripts/check_push_state.py --period morning
echo "=== Afternoon ===" && python3 ~/.openclaw/workspace/skills/daily-learning-push/scripts/check_push_state.py --period afternoon

# 检查heartbeat脚本
echo "=== Heartbeat Check ===" && bash ~/.openclaw/workspace/skills/daily-learning-push/scripts/heartbeat_check.sh
```
