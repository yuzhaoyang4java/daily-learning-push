#!/usr/bin/env python3
"""
推送完成后更新 push-state.json：
用法：update_push_state.py --period morning|afternoon

更新字段：
- lastPushDate / lastMorningPush / lastAfternoonPush
- totalDays +1
- 各方向 index 递增
"""

import json
import os
import argparse
from datetime import date

WORKSPACE = os.environ.get(
    "OPENCLAW_WORKSPACE",
    os.path.expanduser("~/.openclaw/workspace")
)
MEMORY_DIR = os.path.join(WORKSPACE, "memory")
STATE_FILE = os.path.join(MEMORY_DIR, "push-state.json")

os.makedirs(MEMORY_DIR, exist_ok=True)

parser = argparse.ArgumentParser()
parser.add_argument("--period", choices=["morning", "afternoon"], default="morning")
args = parser.parse_args()

today = date.today().isoformat()

# 读取现有状态
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        state = json.load(f)
else:
    state = {
        "lastPushDate": None,
        "lastMorningPush": None,
        "lastAfternoonPush": None,
        "totalDays": 0,
        "totalPushes": 0,
        "nextIndex": {
            "algorithm": 0,
            "algorithm_top100": 0,
            "architecture": 0,
            "ai": 0,
            "technews": 0
        },
        "batchSize": 1  # 每方向每次推送数量
    }

# 更新字段
if args.period == "morning":
    state["lastMorningPush"] = today
else:
    state["lastAfternoonPush"] = today

# 兼容旧格式
state["lastPushDate"] = today
state["totalPushes"] = state.get("totalPushes", 0) + 1

# 每天第一次推送时 totalDays +1
is_first_push_today = (
    state.get("lastMorningPush") != today and 
    state.get("lastAfternoonPush") != today
)
if args.period == "morning" or is_first_push_today:
    state["totalDays"] = state.get("totalDays", 0) + 1

# 更新索引
BATCH_SIZE = state.get("batchSize", 1)
idx = state.get("nextIndex", {})

idx["algorithm"]        = idx.get("algorithm", 0) + BATCH_SIZE
idx["algorithm_top100"] = idx.get("algorithm_top100", 0) + BATCH_SIZE
idx["architecture"]     = idx.get("architecture", 0) + BATCH_SIZE
idx["ai"]               = idx.get("ai", 0) + BATCH_SIZE
idx["technews"]         = idx.get("technews", 0) + 1  # 资讯每次1期(3篇)

state["nextIndex"] = idx

with open(STATE_FILE, "w", encoding="utf-8") as f:
    json.dump(state, f, ensure_ascii=False, indent=2)

print(f"[OK] push-state.json 已更新 ({args.period})")
print(f"  - 上午推送: {state['lastMorningPush']}")
print(f"  - 下午推送: {state['lastAfternoonPush']}")
print(f"  - 累计天数: {state['totalDays']}")
print(f"  - 累计推送: {state['totalPushes']} 次")
print(f"  - 各方向索引: {state['nextIndex']}")
