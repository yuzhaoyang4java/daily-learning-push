#!/usr/bin/env python3
"""
根据 push-state.json 中的当前序号，从主题库中取出今日三方向主题。
输出 JSON 到 stdout，供 agent 使用。
"""

import json
import os
import sys
from datetime import date

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKSPACE = os.environ.get(
    "OPENCLAW_WORKSPACE",
    os.path.expanduser("~/.openclaw/workspace")
)
STATE_FILE = os.path.join(WORKSPACE, "memory", "push-state.json")

# ---------- 读取推送状态 ----------
def load_state():
    if not os.path.exists(STATE_FILE):
        return {
            "lastPushDate": None,
            "totalDays": 0,
            "nextIndex": {"algorithm": 0, "architecture": 0, "ai": 0}
        }
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# ---------- 解析主题库 Markdown ----------
def parse_topic_table(md_path):
    """解析 references/*.md 中的 Markdown 表格，返回 list of dict"""
    topics = []
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_table = False
    headers = []
    for line in lines:
        line = line.strip()
        if line.startswith("| 序号"):
            headers = [h.strip() for h in line.strip("|").split("|")]
            in_table = True
            continue
        if in_table:
            if line.startswith("|---") or not line.startswith("|"):
                if not line.startswith("|"):
                    in_table = False
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 2:
                row = dict(zip(headers, cells))
                topics.append(row)
    return topics

# ---------- 主逻辑 ----------
state = load_state()
idx = state.get("nextIndex", {"algorithm": 0, "architecture": 0, "ai": 0})

algo_path = os.path.join(SKILL_DIR, "references", "algorithm-topics.md")
arch_path = os.path.join(SKILL_DIR, "references", "architecture-topics.md")
ai_path   = os.path.join(SKILL_DIR, "references", "ai-topics.md")

algo_topics = parse_topic_table(algo_path)
arch_topics = parse_topic_table(arch_path)
ai_topics   = parse_topic_table(ai_path)

def get_topic(topics, index):
    if not topics:
        return {"error": "主题库为空"}
    return topics[index % len(topics)]

algo  = get_topic(algo_topics,  idx.get("algorithm", 0))
arch  = get_topic(arch_topics,  idx.get("architecture", 0))
ai    = get_topic(ai_topics,    idx.get("ai", 0))

result = {
    "today": date.today().isoformat(),
    "day": state.get("totalDays", 0) + 1,
    "algorithm": {
        "index": idx.get("algorithm", 0),
        "data": algo
    },
    "architecture": {
        "index": idx.get("architecture", 0),
        "data": arch
    },
    "ai": {
        "index": idx.get("ai", 0),
        "data": ai
    }
}

print(json.dumps(result, ensure_ascii=False, indent=2))
