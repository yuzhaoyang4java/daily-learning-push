#!/usr/bin/bash
# heartbeat_check.sh
# 心跳检查：判断当前时段是否需要推送
# 支持每天两次推送：上午9点 + 下午14点
#
# 用法：heartbeat_check.sh [--period morning|afternoon]
# 返回值：
#   0 + 输出 SHOULD_PUSH_MORNING    → 上午需要推送
#   0 + 输出 SHOULD_PUSH_AFTERNOON   → 下午需要推送  
#   0 + 输出 SKIP_TOO_EARLY         → 时间未到推送时间
#   0 + 输出 ALREADY_PUSHED         → 当前时段已推送
#   0 + 输出 WAIT_NEXT_PERIOD       → 等待下次推送时段

WORKSPACE="${OPENCLAW_WORKSPACE:-$HOME/.openclaw/workspace}"

# 获取当前时间（Asia/Shanghai）
HOUR=$(TZ=Asia/Shanghai date +"%H")
MIN=$(TZ=Asia/Shanghai date +"%M")

# 推送时段配置
MORNING_HOUR=9
AFTERNOON_HOUR=14

# 检查是否为推送窗口时间（前后各5分钟宽容度）
check_push_window() {
    local target_hour=$1
    if [ "$HOUR" -eq "$target_hour" ] || \
       ([ "$HOUR" -eq $((target_hour - 1)) ] && [ "$MIN" -ge 55 ]) || \
       ([ "$HOUR" -eq $((target_hour + 1)) ] && [ "$MIN" -le 5 ]); then
        return 0  # 在推送窗口内
    fi
    return 1  # 不在推送窗口内
}

# 检查上午9点推送
if check_push_window $MORNING_HOUR; then
    RESULT=$(python3 "$WORKSPACE/skills/daily-learning-push/scripts/check_push_state.py" --period morning 2>/dev/null)
    if [ "$RESULT" = "ALREADY_PUSHED" ]; then
        echo "ALREADY_PUSHED_MORNING"
        exit 0
    else
        echo "SHOULD_PUSH_MORNING"
        exit 0
    fi
fi

# 检查下午14点推送  
if check_push_window $AFTERNOON_HOUR; then
    RESULT=$(python3 "$WORKSPACE/skills/daily-learning-push/scripts/check_push_state.py" --period afternoon 2>/dev/null)
    if [ "$RESULT" = "ALREADY_PUSHED" ]; then
        echo "ALREADY_PUSHED_AFTERNOON"
        exit 0
    else
        echo "SHOULD_PUSH_AFTERNOON"
        exit 0
    fi
fi

# 不在任何推送窗口时间
if [ "$HOUR" -lt "$MORNING_HOUR" ]; then
    echo "SKIP_TOO_EARLY (next: ${MORNING_HOUR}:00)"
elif [ "$HOUR" -lt "$AFTERNOON_HOUR" ]; then
    echo "WAIT_NEXT_PERIOD (next: ${AFTERNOON_HOUR}:00)"
else
    echo "WAIT_NEXT_DAY (next: ${MORNING_HOUR}:00 tomorrow)"
fi
