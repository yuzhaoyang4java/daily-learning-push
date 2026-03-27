#!/bin/bash
# sync-remotes.sh - 同步到 GitHub 和 GitLab
# CodeWizHub 版本请手动发布

cd ~/github-daily-learning-push

echo "=== 推送到远程仓库 ==="
echo ""

echo "[1/2] 推送到 GitHub (origin)..."
git push origin main && echo "  ✅ GitHub 成功" || echo "  ❌ GitHub 失败"

echo ""
echo "[2/2] 推送到 GitLab (gitlab)..."
git push gitlab main && echo "  ✅ GitLab 成功" || echo "  ❌ GitLab 失败"

echo ""
echo "=== 同步完成 ==="
echo ""
echo "💡 CodeWizHub 版本请手动发布（如已配置）"
