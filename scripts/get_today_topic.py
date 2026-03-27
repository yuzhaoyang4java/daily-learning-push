#!/usr/bin/env python3
"""
根据 push-state.json 中的当前序号，从主题库中取出今日各时段主题。
用法：get_today_topic.py --period morning|afternoon

每次推送内容：
- 算法 1道（完整题库）
- 算法 1道（Top 100 热题）
- 架构 1篇
- AI 1篇
- 前沿资讯 3篇

时段差异：
- morning: 从当前索引开始
- afternoon: 索引 + 500 偏移（避免与上午重复）
"""

import json
import os
import argparse
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
            "totalPushes": 0,
            "nextIndex": {
                "algorithm": 0,
                "algorithm_top100": 0,
                "architecture": 0,
                "ai": 0,
                "technews": 0
            },
            "batchSize": 1
        }
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        state = json.load(f)
    # 兼容新版本字段名
    idx = state.setdefault("nextIndex", {})
    if "algorithm_top100" not in idx and "top100" in idx:
        idx["algorithm_top100"] = idx["top100"]
    return state

# ---------- 解析主题库 Markdown ----------
def parse_topic_table(md_path, has_link_column=True):
    """解析 references/*.md 中的 Markdown 表格，返回 list of dict"""
    topics = []
    if not os.path.exists(md_path):
        return topics
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_table = False
    headers = []
    for line in lines:
        line = line.strip()
        if line.startswith("|") and ("题号" in line or "序号" in line or "LeetCode" in line):
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
                # 检查是否包含数字（题号或序号）
                first_cell = cells[0].strip()
                if first_cell.isdigit() or (len(cells) > 1 and cells[1].strip().isdigit()):
                    row = dict(zip(headers, cells))
                    topics.append(row)
    return topics

# ---------- 获取单个主题 ----------
def get_topic(topics, index):
    """获取指定索引的主题"""
    if not topics:
        return {"error": "主题库为空", "index": index}
    idx = index % len(topics)
    return topics[idx]

# ---------- 主逻辑 ----------
parser = argparse.ArgumentParser()
parser.add_argument("--period", choices=["morning", "afternoon"], default="morning")
args = parser.parse_args()

state = load_state()
idx = state.get("nextIndex", {})

# 加载所有主题库
algo_path = os.path.join(SKILL_DIR, "references", "algorithm-topics.md")
top100_path = os.path.join(SKILL_DIR, "references", "top100-topics.md")
arch_path = os.path.join(SKILL_DIR, "references", "architecture-topics.md")
ai_path = os.path.join(SKILL_DIR, "references", "ai-topics.md")

algo_topics = parse_topic_table(algo_path)
top100_topics = parse_topic_table(top100_path, has_link_column=True)
arch_topics = parse_topic_table(arch_path, has_link_column=False)
ai_topics = parse_topic_table(ai_path, has_link_column=False)

# 下午时段使用索引偏移，避免重复
DAY_OFFSET = 500 if args.period == "afternoon" else 0

# 获取各方向当前索引（下午+偏移量）
algo_idx = idx.get("algorithm", 0) + DAY_OFFSET
top100_idx = idx.get("algorithm_top100", idx.get("top100", 0)) + DAY_OFFSET
arch_idx = idx.get("architecture", 0) + DAY_OFFSET
ai_idx = idx.get("ai", 0) + DAY_OFFSET

result = {
    "period": args.period,
    "today": date.today().isoformat(),
    "day": state.get("totalDays", 0) + 1,
    "batchSize": 1,
    "contents": {
        "algorithm": {
            "name": "算法 - 完整题库",
            "index": algo_idx,
            "total": len(algo_topics),
            "topic": get_topic(algo_topics, algo_idx),
            "requirement": "题目 + 暴力解→优化解演进 + 完整代码 + 复杂度分析 + 变种题"
        },
        "algorithm_top100": {
            "name": "算法 - 热题 100",
            "index": top100_idx,
            "total": len(top100_topics),
            "topic": get_topic(top100_topics, top100_idx),
            "requirement": "LeetCode热题100，最优解详解，面试重点关注"
        },
        "architecture": {
            "name": "架构设计",
            "index": arch_idx,
            "total": len(arch_topics),
            "topic": get_topic(arch_topics, arch_idx),
            "requirement": "原理 + 架构图 + 代码示例 + 业务场景 + 面试题"
        },
        "ai": {
            "name": "AI 大模型",
            "index": ai_idx,
            "total": len(ai_topics),
            "topic": get_topic(ai_topics, ai_idx),
            "requirement": "概念 + 流程图 + 工程实践 + 业务应用"
        },
        "technews": {
            "name": "前沿技术资讯",
            "index": idx.get("technews", 0),
            "count": 3,
            "requirement": "3篇最新最热技术资讯，每篇：标题+简要总结"
        }
    }
}

print(json.dumps(result, ensure_ascii=False, indent=2))
