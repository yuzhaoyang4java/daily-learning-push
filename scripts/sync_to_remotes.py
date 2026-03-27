#!/usr/bin/env python3
"""
同步代码到远程仓库（GitHub + GitLab）
- 仓库地址从 git remote 读取，不硬编码
- CodeWizHub 请手动发布版本
"""

import subprocess
import sys
import os

def run_cmd(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return result.returncode == 0, result.stdout, result.stderr

def main():
    # 从当前 git 仓库读取 remote，不硬编码地址
    repo_path = os.path.expanduser("~/github-daily-learning-push")

    ok, out, err = run_cmd("git remote -v", cwd=repo_path)
    if not ok:
        print(f"❌ 无法读取 git remote: {err}")
        return 1

    print("=" * 50)
    print("同步 daily-learning-push 到远程仓库")
    print("=" * 50)
    print()

    # 获取所有 remote 名称（排除 codewiz，手动发布）
    ok, out, _ = run_cmd("git remote", cwd=repo_path)
    remotes = [r.strip() for r in out.strip().splitlines()
               if r.strip() and r.strip() != "codewiz"]

    if not remotes:
        print("❌ 未配置任何 remote，请先运行：")
        print("   git remote add origin <your-repo-url>")
        return 1

    results = []
    for i, remote in enumerate(remotes, 1):
        print(f"[{i}/{len(remotes)}] 推送到 {remote}...")
        success, out, err = run_cmd(f"git push {remote} main", cwd=repo_path)
        if success or "Everything up-to-date" in err:
            print(f"  ✅ 成功")
            results.append((remote, True))
        else:
            print(f"  ❌ 失败: {err[:200]}")
            results.append((remote, False))
        print()

    print("=" * 50)
    for remote, success in results:
        print(f"{remote}: {'✅ 成功' if success else '❌ 失败'}")

    print()
    print("💡 CodeWizHub 版本请手动发布：")
    print("   https://codewiz.devops.xiaohongshu.com/hub/daily-learning-push")

    return 0 if all(s for _, s in results) else 1

if __name__ == "__main__":
    sys.exit(main())
