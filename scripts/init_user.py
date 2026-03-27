#!/usr/bin/env python3
"""
首次初始化脚本 - 新用户运行此脚本完成配置
1. 自动创建 Redoc 学习空间父文档
2. 生成 memory/.redoc-config.json
3. 初始化 push-state.json
"""

import json
import os
import subprocess
import sys

MEMORY_DIR = os.path.expanduser("~/.openclaw/workspace/memory")
REDOC_CONFIG = os.path.join(MEMORY_DIR, ".redoc-config.json")
PUSH_STATE = os.path.join(MEMORY_DIR, "push-state.json")
REDOC_SKILL = "/app/skills/hi-redoc-curd/scripts/hi-redoc-curd.sh"

INIT_PARENT_DOC = """# 📚 我的技术学习空间

> 由 daily-learning-push skill 自动创建并维护

## 学习档案索引

| 日期 | 时段 | 主题摘要 | 文档链接 |
|------|------|----------|----------|
| (首次推送后自动填充) | - | - | - |

---

*每天 9:00 和 14:00 自动推送，内容包含：算法题×2 + 架构专题 + AI专题 + 前沿资讯×3*
"""

def create_redoc_parent():
    """自动创建 Redoc 父文档"""
    print("📄 正在创建你的学习空间父文档...")

    # 写临时文件
    tmp_file = "/tmp/init-learning-space.md"
    with open(tmp_file, "w") as f:
        f.write(INIT_PARENT_DOC)

    result = subprocess.run(
        ["bash", REDOC_SKILL, "-p", tmp_file],
        capture_output=True, text=True
    )

    try:
        data = json.loads(result.stdout)
        if data.get("success"):
            shortcut_id = data["data"]["shortcutId"]
            doc_url = data["data"]["docUrl"]
            print(f"  ✅ 创建成功！")
            print(f"  📎 文档地址: {doc_url}")
            return shortcut_id, doc_url
        else:
            print(f"  ❌ 创建失败: {data}")
    except Exception as e:
        print(f"  ❌ 解析失败: {e}\n  原始输出: {result.stdout[:200]}")

    return None, None

def init_redoc_config(shortcut_id, doc_url):
    """初始化 Redoc 配置"""
    os.makedirs(MEMORY_DIR, exist_ok=True)
    config = {
        "parentDocId": shortcut_id,
        "parentDocUrl": doc_url,
        "enabled": True,
        "autoUpdateIndex": True,
        "createdAt": __import__('datetime').date.today().isoformat()
    }
    with open(REDOC_CONFIG, "w") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    print(f"  💾 配置已保存到 memory/.redoc-config.json")

def init_push_state():
    """初始化推送状态"""
    if os.path.exists(PUSH_STATE):
        print(f"  ℹ️  push-state.json 已存在，跳过初始化")
        return

    state = {
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
        "redocHistory": []
    }
    os.makedirs(MEMORY_DIR, exist_ok=True)
    with open(PUSH_STATE, "w") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    print(f"  💾 push-state.json 已初始化（从 Day 1 开始）")

def check_already_initialized():
    """检查是否已经初始化过"""
    if os.path.exists(REDOC_CONFIG):
        with open(REDOC_CONFIG) as f:
            config = json.load(f)
        if config.get("parentDocId"):
            return True, config
    return False, None

def main():
    print("=" * 55)
    print("  daily-learning-push · 首次初始化")
    print("=" * 55)
    print()

    # 检查是否已初始化
    initialized, config = check_already_initialized()
    if initialized:
        print(f"✅ 已初始化过，学习空间父文档：")
        print(f"   {config.get('parentDocUrl', config.get('parentDocId'))}")
        print()
        ans = input("是否重新初始化？(y/N): ").strip().lower()
        if ans != "y":
            print("跳过初始化。")
            return 0

    # Step 1: 创建 Redoc 父文档
    if not os.path.exists(REDOC_SKILL):
        print("⚠️  未找到 hi-redoc-curd skill，跳过 Redoc 创建")
        print("   请先安装 hi-redoc-curd skill，或手动配置 memory/.redoc-config.json")
        shortcut_id, doc_url = None, None
    else:
        shortcut_id, doc_url = create_redoc_parent()

    # Step 2: 保存配置
    if shortcut_id:
        init_redoc_config(shortcut_id, doc_url)
    else:
        print()
        print("⚠️  Redoc 未配置，推送内容将仅保存本地。")
        print("   如需启用，请手动编辑：memory/.redoc-config.json")
        os.makedirs(MEMORY_DIR, exist_ok=True)
        with open(REDOC_CONFIG, "w") as f:
            json.dump({"enabled": False, "parentDocId": None}, f, indent=2)

    # Step 3: 初始化推送状态
    print()
    init_push_state()

    print()
    print("=" * 55)
    print("  初始化完成！")
    print("=" * 55)
    print()
    print("后续操作：")
    print("  - 等待每天 9:00 / 14:00 自动推送")
    print("  - 或对 OpenClaw 说「今日学习」手动触发")
    if doc_url:
        print(f"  - 查看学习空间：{doc_url}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
