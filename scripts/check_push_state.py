#!/usr/bin/env python3
"""
检查当前时段是否已推送。
用法：check_push_state.py --period morning|afternoon
输出：
  ALREADY_PUSHED  — 当前时段已推送
  NOT_PUSHED      — 当前时段未推送
"""

import json
import os
import sys
import argparse
from datetime import date

WORKSPACE = os.environ.get(
    "OPENCLAW_WORKSPACE",
    os.path.expanduser("~/.openclaw/workspace")
)
STATE_FILE = os.path.join(WORKSPACE, "memory", "push-state.json")

parser = argparse.ArgumentParser()
parser.add_argument("--period", choices=["morning", "afternoon"], default="morning")
args = parser.parse_args()

today = date.today().isoformat()

if not os.path.exists(STATE_FILE):
    print("NOT_PUSHED")
    sys.exit(0)

with open(STATE_FILE, "r", encoding="utf-8") as f:
    state = json.load(f)

# 支持旧格式（单时段）和新格式（分时段）
if args.period == "morning":
    last_push = state.get("lastMorningPush") or state.get("lastPushDate")
else:
    last_push = state.get("lastAfternoonPush")

if last_push == today:
    print("ALREADY_PUSHED")
else:
    print("NOT_PUSHED")
