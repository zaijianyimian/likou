from collections import defaultdict
from typing import Optional

# 路径总和。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.cnt = defaultdict(int) # 利用前缀和解决
        self.ans = 0
        self.cnt[0] = 1
        self.dfs(root, 0, targetSum)
        return self.ans

    def dfs(self, node: Optional[TreeNode], s: int, targetSum: int) -> None:
        if node is None:
            return
        s += node.val
        self.ans += self.cnt[s - targetSum]

        self.cnt[s] += 1
        self.dfs(node.left, s, targetSum)
        self.dfs(node.right, s, targetSum)
        self.cnt[s] -= 1
