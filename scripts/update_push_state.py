#!/usr/bin/env python3
"""
推送完成后更新 push-state.json：
- 更新 lastPushDate 为今天
- totalDays + 1
- 五方向 index 各 + batchSize (默认4)
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
        "nextIndex": {
            "algorithm": 0,
            "top100": 0,
            "architecture": 0,
            "ai": 0,
            "technews": 0
        },
        "batchSize": 4  # 每方向推送数量
    }

# 更新状态
BATCH_SIZE = state.get("batchSize", 4)
state["lastPushDate"] = date.today().isoformat()
state["totalDays"] = state.get("totalDays", 0) + 1

idx = state.get("nextIndex", {})
# 五方向索引各加 batchSize
idx["algorithm"]    = idx.get("algorithm", 0) + BATCH_SIZE
idx["top100"]       = idx.get("top100", 0) + BATCH_SIZE
idx["architecture"] = idx.get("architecture", 0) + BATCH_SIZE
idx["ai"]           = idx.get("ai", 0) + BATCH_SIZE
idx["technews"]     = idx.get("technews", 0) + 1  # 资讯每天1期

state["nextIndex"] = idx

with open(STATE_FILE, "w", encoding="utf-8") as f:
    json.dump(state, f, ensure_ascii=False, indent=2)

print(f"[OK] push-state.json 已更新：")
print(f"  - 推送日期: {state['lastPushDate']}")
print(f"  - 累计天数: {state['totalDays']}")
print(f"  - 各方向索引: {state['nextIndex']}")
