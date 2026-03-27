#!/bin/bash
# auto_switch_heartbeat.sh - 根据时段自动切换心跳频率

set -e

CONFIG_FILE="$HOME/.openclaw/openclaw.json"
LOG_FILE="$HOME/.openclaw/logs/heartbeat_switch.log"

# 创建日志目录
mkdir -p "$HOME/.openclaw/logs"

# 获取当前时间
HOUR=$(TZ=Asia/Shanghai date +"%H")
DAY=$(TZ=Asia/Shanghai date +"%u")  # 1-5 周一到周五

# 判断当前时段
IS_WORKDAY=false
if [ "$DAY" -ge 1 ] && [ "$DAY" -le 5 ]; then
    IS_WORKDAY=true
fi

IS_WORK_HOURS=false
if [ "$HOUR" -ge 8 ] && [ "$HOUR" -lt 18 ]; then
    IS_WORK_HOURS=true
fi

# 确定目标频率
if [ "$IS_WORKDAY" = true ] && [ "$IS_WORK_HOURS" = true ]; then
    TARGET_FREQ="15m"
    TARGET_DESC="高频（工作日 08:00-18:00）"
else
    TARGET_FREQ="1h"
    if [ "$IS_WORKDAY" = false ]; then
        TARGET_DESC="低频（周末）"
    else
        TARGET_DESC="低频（夜间 18:00-次日 08:00）"
    fi
fi

# 获取当前频率
CURRENT_FREQ=$(python3 -c "
import json
import sys
try:
    with open('$CONFIG_FILE', 'r') as f:
        config = json.load(f)
    print(config.get('agents', {}).get('defaults', {}).get('heartbeat', {}).get('every', 'unknown'))
except Exception as e:
    print('unknown')
")

if [ "$CURRENT_FREQ" = "$TARGET_FREQ" ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 当前已是 $TARGET_FREQ，无需切换 ($TARGET_DESC)" >> "$LOG_FILE"
    echo "CURRENT:$TARGET_FREQ"
    exit 0
fi

# 需要切换，备份并修改配置
BACKUP_FILE="$HOME/.openclaw/openclaw.json.backup.$(date +%Y%m%d%H%M%S)"
cp "$CONFIG_FILE" "$BACKUP_FILE"

python3 << PYEOF
import json
import sys

config_file = "$CONFIG_FILE"

with open(config_file, 'r', encoding='utf-8') as f:
    config = json.load(f)

config['agents']['defaults']['heartbeat']['every'] = '$TARGET_FREQ'

with open(config_file, 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

print(f"[$(date '+%Y-%m-%d %H:%M:%S')] 心跳间隔已从 $CURRENT_FREQ 切换为 $TARGET_FREQ ($TARGET_DESC)")
PYEOF

echo "[$(date '+%Y-%m-%d %H:%M:%S')] 已切换: $CURRENT_FREQ → $TARGET_FREQ ($TARGET_DESC)" >> "$LOG_FILE"

# 重启 Gateway 使配置生效
openclaw gateway restart 2>&1 | tee -a "$LOG_FILE"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Gateway 已重启" >> "$LOG_FILE"
echo "SWITCHED:$TARGET_FREQ"
