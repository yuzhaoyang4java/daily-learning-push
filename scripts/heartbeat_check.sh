#!/usr/bin/env bash
# heartbeat_check.sh
# 心跳检查：判断今日是否需要推送
# 返回值：
#   0 + 输出 SHOULD_PUSH   → 需要推送（今日未推送且已过 09:00）
#   0 + 输出 SKIP_TOO_EARLY → 时间未到 09:00，跳过
#   0 + 输出 ALREADY_PUSHED → 今日已推送，跳过

WORKSPACE="${OPENCLAW_WORKSPACE:-$HOME/.openclaw/workspace}"

# 当前小时（24 小时制，Asia/Shanghai）
HOUR=$(TZ=Asia/Shanghai date +"%H")

if [ "$HOUR" -lt 9 ]; then
  echo "SKIP_TOO_EARLY"
  exit 0
fi

# 调用 Python 脚本判断状态
RESULT=$(python3 "$WORKSPACE/skills/daily-learning-push/scripts/check_push_state.py")

if [ "$RESULT" = "ALREADY_PUSHED" ]; then
  echo "ALREADY_PUSHED"
else
  echo "SHOULD_PUSH"
fi
