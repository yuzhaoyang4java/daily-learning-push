#!/usr/bin/env python3
"""
检查今日是否已推送。
输出：
  ALREADY_PUSHED  — 今日已推送
  NOT_PUSHED      — 今日未推送
"""

import json
import os
import sys
from datetime import date

WORKSPACE = os.environ.get(
    "OPENCLAW_WORKSPACE",
    os.path.expanduser("~/.openclaw/workspace")
)
STATE_FILE = os.path.join(WORKSPACE, "memory", "push-state.json")

today = date.today().isoformat()

if not os.path.exists(STATE_FILE):
    print("NOT_PUSHED")
    sys.exit(0)

with open(STATE_FILE, "r", encoding="utf-8") as f:
    state = json.load(f)

if state.get("lastPushDate") == today:
    print("ALREADY_PUSHED")
else:
    print("NOT_PUSHED")
