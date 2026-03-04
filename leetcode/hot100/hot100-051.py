from typing import Optional

# 124 二叉树中的最大路径和
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution: # 后序遍历，左中右
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return 0
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)
            curSUm = node.val + left + right
            self.maxSum = max(self.maxSum,curSUm)
            return node.val + max(left,right)
        dfs( root)
        return self.maxSum

