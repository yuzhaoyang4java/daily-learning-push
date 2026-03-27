#!/usr/bin/env python3
"""
读取 Redoc 配置
方便脚本调用获取配置信息
"""

import json
import os

def get_redoc_config():
    """读取 Redoc 配置文件"""
    config_path = os.path.expanduser("~/.openclaw/workspace/memory/.redoc-config.json")
    
    if not os.path.exists(config_path):
        return {
            "enabled": False,
            "parentDocId": None,
            "description": "未配置"
        }
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config
    except Exception as e:
        return {
            "enabled": False,
            "error": str(e)
        }

def main():
    import sys
    
    config = get_redoc_config()
    
    # 支持命令行参数输出特定字段
    if len(sys.argv) > 1:
        field = sys.argv[1]
        print(config.get(field, ""))
        return
    
    # 默认输出完整配置
    print(json.dumps(config, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
