#!/usr/bin/env python3
"""
根据 push-state.json 中的当前序号，从主题库中取出今日五方向主题。
输出 JSON 到 stdout，供 agent 使用。

五方向：
1. 算法 - 完整题库（2000+体系）
2. 算法 - Top 100 热题
3. 架构
4. AI
5. 前沿技术资讯

每方向至少推送4篇详细内容。
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
            "nextIndex": {
                "algorithm": 0,      # 完整题库索引
                "top100": 0,         # Top 100 索引
                "architecture": 0, 
                "ai": 0, 
                "technews": 0
            }
        }
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        state = json.load(f)
    # 兼容旧版本
    idx = state.setdefault("nextIndex", {})
    if "top100" not in idx:
        idx["top100"] = 0
    return state

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
            if len(cells) >= 2 and cells[0].isdigit():
                row = dict(zip(headers, cells))
                topics.append(row)
    return topics

# ---------- 获取多个连续主题 ----------
def get_topics_batch(topics, start_index, batch_size=4):
    """获取从 start_index 开始的 batch_size 个主题"""
    if not topics:
        return [{"error": "主题库为空"}]
    result = []
    for i in range(batch_size):
        idx = (start_index + i) % len(topics)
        result.append(topics[idx])
    return result

# ---------- 主逻辑 ----------
state = load_state()
idx = state.get("nextIndex", {})

# 加载所有主题库
algo_path = os.path.join(SKILL_DIR, "references", "algorithm-topics.md")
top100_path = os.path.join(SKILL_DIR, "references", "top100-topics.md")
arch_path = os.path.join(SKILL_DIR, "references", "architecture-topics.md")
ai_path = os.path.join(SKILL_DIR, "references", "ai-topics.md")

algo_topics = parse_topic_table(algo_path)
top100_topics = parse_topic_table(top100_path)
arch_topics = parse_topic_table(arch_path)
ai_topics = parse_topic_table(ai_path)

# 获取各方向当前索引
algo_idx = idx.get("algorithm", 0)
top100_idx = idx.get("top100", 0)
arch_idx = idx.get("architecture", 0)
ai_idx = idx.get("ai", 0)

result = {
    "today": date.today().isoformat(),
    "day": state.get("totalDays", 0) + 1,
    "batchSize": 4,  # 每个方向推送4篇
    "directions": {
        "algorithm": {
            "name": "算法 - 完整题库",
            "index": algo_idx,
            "total": len(algo_topics),
            "topics": get_topics_batch(algo_topics, algo_idx, 4),
            "requirement": "4道算法题，每题包含：暴力解→优化解演进、完整代码、复杂度分析、图解、变种题、面试追问"
        },
        "top100": {
            "name": "算法 - Top 100 热题",
            "index": top100_idx,
            "total": len(top100_topics),
            "topics": get_topics_batch(top100_topics, top100_idx, 4),
            "requirement": "4道LeetCode热题100题目，重点突破，详细讲解最优解"
        },
        "architecture": {
            "name": "架构设计",
            "index": arch_idx,
            "total": len(arch_topics),
            "topics": get_topics_batch(arch_topics, arch_idx, 4),
            "requirement": "4个架构主题，每个包含：原理详解、架构图、代码示例、业务场景、面试题"
        },
        "ai": {
            "name": "AI 大模型",
            "index": ai_idx,
            "total": len(ai_topics),
            "topics": get_topics_batch(ai_topics, ai_idx, 4),
            "requirement": "4个AI主题，每个包含：概念解释、流程图、工程实践、业务应用、评估指标"
        },
        "technews": {
            "name": "前沿技术资讯",
            "index": idx.get("technews", 0),
            "enabled": True,
            "minArticles": 4,
            "categories": ["前沿技术迭代", "架构设计", "AI大模型"],
            "requirement": "至少4篇最新最热技术资讯，每篇包含：来源、摘要、要点、链接、标签"
        }
    }
}

print(json.dumps(result, ensure_ascii=False, indent=2))
