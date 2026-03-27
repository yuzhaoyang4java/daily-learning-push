#!/usr/bin/env python3
"""
推送完成后更新 push-state.json：
- 更新 lastPushDate 为今天
- totalDays + 1
- 三方向 index 各 + 1
"""

import json
import os
from datetime import date

WORKSPACE = os.environ.get(
    "OPENCLAW_WORKSPACE",
    os.path.expanduser("~/.openclaw/workspace")
)
MEMORY_DIR = os.path.join(WORKSPACE, "memory")
STATE_FILE = os.path.join(MEMORY_DIR, "push-state.json")

os.makedirs(MEMORY_DIR, exist_ok=True)

# 读取现有状态
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        state = json.load(f)
else:
    state = {
        "lastPushDate": None,
        "totalDays": 0,
        "nextIndex": {"algorithm": 0, "architecture": 0, "ai": 0}
    }

# 更新状态
state["lastPushDate"] = date.today().isoformat()
state["totalDays"] = state.get("totalDays", 0) + 1
idx = state.get("nextIndex", {"algorithm": 0, "architecture": 0, "ai": 0})
idx["algorithm"]    = idx.get("algorithm", 0) + 1
idx["architecture"] = idx.get("architecture", 0) + 1
idx["ai"]           = idx.get("ai", 0) + 1
state["nextIndex"] = idx

with open(STATE_FILE, "w", encoding="utf-8") as f:
    json.dump(state, f, ensure_ascii=False, indent=2)

print(f"[OK] push-state.json 已更新：{state}")
