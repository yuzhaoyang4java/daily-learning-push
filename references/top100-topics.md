# LeetCode 热题 100 题目库（完整链接版）

来源：https://leetcode.cn/studyplan/top-100-liked/

最受刷题发烧友欢迎的 100 道题，面试高频必刷。
**所有链接均已验证可访问：** `https://leetcode.cn/problems/{slug}/`

---

## 题目列表（按分类组织）

### 哈希（3题）
| 序号 | LeetCode | 题目 | 链接 | 难度 | 核心考点 |
|------|---------|------|------|------|---------|
| 1 | 1 | 两数之和 | https://leetcode.cn/problems/two-sum/ | Easy | HashMap 一次遍历 |
| 2 | 49 | 字母异位词分组 | https://leetcode.cn/problems/group-anagrams/ | Medium | 排序作为键/字符计数 |
| 3 | 128 | 最长连续序列 | https://leetcode.cn/problems/longest-consecutive-sequence/ | Medium | HashSet 跳过非起点 |

### 双指针（6题）
| 序号 | LeetCode | 题目 | 链接 | 难度 | 核心考点 |
|------|---------|------|------|------|---------|
| 4 | 283 | 移动零 | https://leetcode.cn/problems/move-zeroes/ | Easy | 快慢指针交换 |
| 5 | 11 | 盛最多水的容器 | https://leetcode.cn/problems/container-with-most-water/ | Medium | 左右指针向中间收敛 |
| 6 | 15 | 三数之和 | https://leetcode.cn/problems/3sum/ | Medium | 排序+双指针去重 |
| 7 | 42 | 接雨水 | https://leetcode.cn/problems/trapping-rain-water/ | Hard | 左右最大高度差 |
| 8 | 240 | 搜索二维矩阵 II | https://leetcode.cn/problems/search-a-2d-matrix-ii/ | Medium | 从右上搜索 |
| 9 | 4 | 寻找两个正序数组的中位数 | https://leetcode.cn/problems/median-of-two-sorted-arrays/ | Hard | 划分数组 |

### 滑动窗口（5题）
| 序号 | LeetCode | 题目 | 链接 | 难度 | 核心考点 |
|------|---------|------|------|------|---------|
| 10 | 3 | 无重复字符的最长子串 | https://leetcode.cn/problems/longest-substring-without-repeating-characters/ | Medium | HashSet双指针 |
| 11 | 438 | 找到字符串中所有字母异位词 | https://leetcode.cn/problems/find-all-anagrams-in-a-string/ | Medium | 固定长度滑窗+数组计数 |
| 12 | 560 | 和为K的子数组 | https://leetcode.cn/problems/subarray-sum-equals-k/ | Medium | 前缀和+哈希 |
| 13 | 239 | 滑动窗口最大值 | https://leetcode.cn/problems/sliding-window-maximum/ | Hard | 单调队列 |
| 14 | 76 | 最小覆盖子串 | https://leetcode.cn/problems/minimum-window-substring/ | Hard | 可变窗口满足条件 |

### 子串/子序列/子数组（6题）
| 序号 | LeetCode | 题目 | 链接 | 难度 | 核心考点 |
|------|---------|------|------|------|---------|
| 15 | 53 | 最大子数组和 | https://leetcode.cn/problems/maximum-subarray/ | Medium | Kadane算法/前缀和 |
| 16 | 56 | 合并区间 | https://leetcode.cn/problems/merge-intervals/ | Medium | 按起点排序后合并 |
| 17 | 189 | 轮转数组 | https://leetcode.cn/problems/rotate-array/ | Medium | 三次翻转法 |
| 18 | 238 | 除自身以外数组的乘积 | https://leetcode.cn/problems/product-of-array-except-self/ | Medium | 左积×右积 |
| 19 | 41 | 缺失的第一个正数 | https://leetcode.cn/problems/first-missing-positive/ | Hard | 原地哈希/鸽巢原理 |
| 20 | 73 | 矩阵置零 | https://leetcode.cn/problems/set-matrix-zeroes/ | Medium | 标记第一行/列 |

### 栈（6题）
| 序号 | LeetCode | 题目 | 链接 | 难度 | 核心考点 |
|------|---------|------|------|------|---------|
| 21 | 20 | 有效的括号 | https://leetcode.cn/problems/valid-parentheses/ | Easy | 栈匹配 |
| 22 | 155 | 最小栈 | https://leetcode.cn/problems/min-stack/ | Medium | 辅助栈维护最小值 |
| 23 | 394 | 字符串解码 | https://leetcode.cn/problems/decode-string/ | Medium | 栈模拟嵌套解码 |
| 24 | 739 | 每日温度 | https://leetcode.cn/problems/daily-temperatures/ | Medium | 单调栈找下一个更大 |
| 25 | 84 | 柱状图中最大的矩形 | https://leetcode.cn/problems/largest-rectangle-in-histogram/ | Hard | 单调栈找左右边界 |
| 26 | 85 | 最大矩形 | https://leetcode.cn/problems/maximal-rectangle/ | Hard | 单调栈+逐行处理 |

### 链表（9题）
| 序号 | LeetCode | 题目 | 链接 | 难度 | 核心考点 |
|------|---------|------|------|------|---------|
| 27 | 21 | 合并两个有序链表 | https://leetcode.cn/problems/merge-two-sorted-lists/ | Easy | 递归/迭代双指针 |
| 28 | 206 | 反转链表 | https://leetcode.cn/problems/reverse-linked-list/ | Easy | 迭代三指针/递归 |
| 29 | 141 | 环形链表 | https://leetcode.cn/problems/linked-list-cycle/ | Easy | Floyd快慢指针 |
| 30 | 142 | 环形链表 II | https://leetcode.cn/problems/linked-list-cycle-ii/ | Medium | 找环入口数学推导 |
| 31 | 160 | 相交链表 | https://leetcode.cn/problems/intersection-of-two-linked-lists/ | Easy | 双指针等长对齐 |
| 32 | 19 | 删除链表的倒数第 N 个结点 | https://leetcode.cn/problems/remove-nth-node-from-end-of-list/ | Medium | 快慢指针间距N |
| 33 | 2 | 两数相加 | https://leetcode.cn/problems/add-two-numbers/ | Medium | 模拟竖式加法 |
| 34 | 24 | 两两交换链表中的节点 | https://leetcode.cn/problems/swap-nodes-in-pairs/ | Medium | 迭代/递归交换 |
| 35 | 148 | 排序链表 | https://leetcode.cn/problems/sort-list/ | Medium | 归并排序链表版 |

### 二叉树（15题）
| 序号 | LeetCode | 题目 | 链接 | 难度 | 核心考点 |
|------|---------|------|------|------|---------|
| 36 | 94 | 二叉树的中序遍历 | https://leetcode.cn/problems/binary-tree-inorder-traversal/ | Easy | 递归+迭代栈模拟 |
| 37 | 104 | 二叉树的最大深度 | https://leetcode.cn/problems/maximum-depth-of-binary-tree/ | Easy | 递归后序遍历 |
| 38 | 226 | 翻转二叉树 | https://leetcode.cn/problems/invert-binary-tree/ | Easy | 递归交换左右子树 |
| 39 | 101 | 对称二叉树 | https://leetcode.cn/problems/symmetric-tree/ | Easy | 递归比较镜像节点 |
| 40 | 543 | 二叉树的直径 | https://leetcode.cn/problems/diameter-of-binary-tree/ | Easy | 后序遍历全局变量 |
| 41 | 102 | 二叉树的层序遍历 | https://leetcode.cn/problems/binary-tree-level-order-traversal/ | Medium | 队列BFS层次遍历 |
| 42 | 108 | 将有序数组转换为二叉搜索树 | https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/ | Easy | 中点作为根递归构建 |
| 43 | 98 | 验证二叉搜索树 | https://leetcode.cn/problems/validate-binary-search-tree/ | Medium | 递归验证区间 |
| 44 | 230 | 二叉搜索树中第K小的元素 | https://leetcode.cn/problems/kth-smallest-element-in-a-bst/ | Medium | 中序遍历计数 |
| 45 | 199 | 二叉树的右视图 | https://leetcode.cn/problems/binary-tree-right-side-view/ | Medium | 层序遍历取最右 |
| 46 | 114 | 二叉树展开为链表 | https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/ | Medium | 递归展开调整指针 |
| 47 | 105 | 从前序与中序遍历序列构造二叉树 | https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/ | Medium | 递归分治构建 |
| 48 | 437 | 路径总和 III | https://leetcode.cn/problems/path-sum-iii/ | Medium | DFS+前缀和哈希 |
| 49 | 236 | 二叉树的最近公共祖先 | https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/ | Medium | 后序遍历LCA |
| 50 | 124 | 二叉树中的最大路径和 | https://leetcode.cn/problems/binary-tree-maximum-path-sum/ | Hard | 后序遍历+全局变量 |

### 图论（6题）
| 序号 | LeetCode | 题目 | 链接 | 难度 | 核心考点 |
|------|---------|------|------|------|---------|
| 51 | 200 | 岛屿数量 | https://leetcode.cn/problems/number-of-islands/ | Medium | DFS标记/BFS/并查集 |
| 52 | 994 | 腐烂的橘子 | https://leetcode.cn/problems/rotting-oranges/ | Medium | 多源BFS |
| 53 | 207 | 课程表 | https://leetcode.cn/problems/course-schedule/ | Medium | 拓扑排序DFS/BFS |
| 54 | 210 | 课程表 II | https://leetcode.cn/problems/course-schedule-ii/ | Medium | 拓扑排序+记录顺序 |
| 55 | 133 | 克隆图 | https://leetcode.cn/problems/clone-graph/ | Medium | DFS/BFS复制节点 |
| 56 | 261 | 以图判树 | https://leetcode.cn/problems/graph-valid-tree/ | Medium | 并查集/DFS判环 |

### 二分查找（7题）
| 序号 | LeetCode | 题目 | 链接 | 难度 | 核心考点 |
|------|---------|------|------|------|---------|
| 57 | 33 | 搜索旋转排序数组 | https://leetcode.cn/problems/search-in-rotated-sorted-array/ | Medium | 判断哪一半有序 |
| 58 | 153 | 寻找旋转排序数组中的最小值 | https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/ | Medium | 比较mid和right |
| 59 | 35 | 搜索插入位置 | https://leetcode.cn/problems/search-insert-position/ | Easy | 标准lower_bound |
| 60 | 74 | 搜索二维矩阵 | https://leetcode.cn/problems/search-a-2d-matrix/ | Medium | 二维转一维二分 |
| 61 | 34 | 在排序数组中查找元素的第一个和最后一个位置 | https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/ | Medium | 找左右边界 |
| 62 | 4 | 寻找两个正序数组的中位数 | https://leetcode.cn/problems/median-of-two-sorted-arrays/ | Hard | 划分数组二分 |
| 63 | 378 | 有序矩阵中第K小的元素 | https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/ | Medium | 二分答案值 |

### 回溯（8题）
| 序号 | LeetCode | 题目 | 链接 | 难度 | 核心考点 |
|------|---------|------|------|------|---------|
| 64 | 46 | 全排列 | https://leetcode.cn/problems/permutations/ | Medium | 回溯模板+去重 |
| 65 | 78 | 子集 | https://leetcode.cn/problems/subsets/ | Medium | 回溯枚举所有子集 |
| 66 | 17 | 电话号码的字母组合 | https://leetcode.cn/problems/letter-combinations-of-a-phone-number/ | Medium | 递归构造组合 |
| 67 | 39 | 组合总和 | https://leetcode.cn/problems/combination-sum/ | Medium | 回溯求所有组合 |
| 68 | 22 | 括号生成 | https://leetcode.cn/problems/generate-parentheses/ | Medium | 递归生成括号卡特兰数 |
| 69 | 51 | N皇后 | https://leetcode.cn/problems/n-queens/ | Hard | 经典回溯问题 |
| 70 | 79 | 单词搜索 | https://leetcode.cn/problems/word-search/ | Medium | DFS二维网格+回溯 |
| 71 | 131 | 分割回文串 | https://leetcode.cn/problems/palindrome-partitioning/ | Medium | 回溯+DP预处理 |

### 动态规划（14题）
| 序号 | LeetCode | 题目 | 链接 | 难度 | 核心考点 |
|------|---------|------|------|------|---------|
| 72 | 70 | 爬楼梯 | https://leetcode.cn/problems/climbing-stairs/ | Easy | DP入门斐波那契变形 |
| 73 | 118 | 杨辉三角 | https://leetcode.cn/problems/pascals-triangle/ | Easy | 递推构造 |
| 74 | 198 | 打家劫舍 | https://leetcode.cn/problems/house-robber/ | Medium | DP选或不选状态转移 |
| 75 | 279 | 完全平方数 | https://leetcode.cn/problems/perfect-squares/ | Medium | DP/BFS最短路 |
| 76 | 322 | 零钱兑换 | https://leetcode.cn/problems/coin-change/ | Medium | 完全背包变形 |
| 77 | 139 | 单词拆分 | https://leetcode.cn/problems/word-break/ | Medium | 前缀DP |
| 78 | 300 | 最长递增子序列 | https://leetcode.cn/problems/longest-increasing-subsequence/ | Medium | DP/二分+贪心 |
| 79 | 152 | 乘积最大子数组 | https://leetcode.cn/problems/maximum-product-subarray/ | Medium | 同时维护最大最小值 |
| 80 | 416 | 分割等和子集 | https://leetcode.cn/problems/partition-equal-subset-sum/ | Medium | 0/1背包 |
| 81 | 1143 | 最长公共子序列 | https://leetcode.cn/problems/longest-common-subsequence/ | Medium | 二维DP LCS |
| 82 | 72 | 编辑距离 | https://leetcode.cn/problems/edit-distance/ | Hard | 二维DP状态转移 |
| 83 | 5 | 最长回文子串 | https://leetcode.cn/problems/longest-palindromic-substring/ | Medium | DP/中心扩展 |
| 84 | 647 | 回文子串 | https://leetcode.cn/problems/palindromic-substrings/ | Medium | 中心扩展累计计数 |
| 85 | 32 | 最长有效括号 | https://leetcode.cn/problems/longest-valid-parentheses/ | Hard | DP/栈找匹配 |

### 贪心（5题）
| 序号 | LeetCode | 题目 | 链接 | 难度 | 核心考点 |
|------|---------|------|------|------|---------|
| 86 | 121 | 买卖股票的最佳时机 | https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/ | Easy | 维护历史最低价 |
| 87 | 55 | 跳跃游戏 | https://leetcode.cn/problems/jump-game/ | Medium | 维护最远可达位置 |
| 88 | 45 | 跳跃游戏 II | https://leetcode.cn/problems/jump-game-ii/ | Medium | 记录当前和下次边界 |
| 89 | 435 | 无重叠区间 | https://leetcode.cn/problems/non-overlapping-intervals/ | Medium | 贪心最早结束 |
| 90 | 56 | 合并区间 | https://leetcode.cn/problems/merge-intervals/ | Medium | 按起点排序后合并 |

### 设计（5题）
| 序号 | LeetCode | 题目 | 链接 | 难度 | 核心考点 |
|------|---------|------|------|------|---------|
| 91 | 146 | LRU缓存 | https://leetcode.cn/problems/lru-cache/ | Medium | HashMap+双向链表 |
| 92 | 380 | O(1) 时间插入、删除和获取随机元素 | https://leetcode.cn/problems/insert-delete-getrandom-o1/ | Medium | HashMap+ArrayList |
| 93 | 208 | 实现 Trie (前缀树) | https://leetcode.cn/problems/implement-trie-prefix-tree/ | Medium | 多叉树字母节点 |
| 94 | 295 | 数据流的中位数 | https://leetcode.cn/problems/find-median-from-data-stream/ | Hard | 大顶堆+小顶堆 |
| 95 | 225 | 用队列实现栈 | https://leetcode.cn/problems/implement-stack-using-queues/ | Easy | 两个队列/一个队列 |

### 其他高频（5题）
| 序号 | LeetCode | 题目 | 链接 | 难度 | 核心考点 |
|------|---------|------|------|------|---------|
| 96 | 136 | 只出现一次的数字 | https://leetcode.cn/problems/single-number/ | Easy | 异或运算 |
| 97 | 169 | 多数元素 | https://leetcode.cn/problems/majority-element/ | Easy | 摩尔投票 |
| 98 | 215 | 数组中的第K个最大元素 | https://leetcode.cn/problems/kth-largest-element-in-an-array/ | Medium | 快选/堆 |
| 99 | 347 | 前K个高频元素 | https://leetcode.cn/problems/top-k-frequent-elements/ | Medium | 堆/桶排序 |
| 100 | 31 | 下一个排列 | https://leetcode.cn/problems/next-permutation/ | Medium | 从后找第一对小数交换 |

---

## 学习计划链接

- **LeetCode 热题 100 学习计划页面**: https://leetcode.cn/studyplan/top-100-liked/
- **完整题库页面**: https://leetcode.cn/problemset/

## 使用说明

1. **直接点击链接**即可访问题目页面
2. **面试冲刺**：按分类集中突破，理解解题套路
3. **每日推送**：配合学习计划，系统刷题
