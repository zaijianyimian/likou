from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sum = float('-inf')

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            # curSum表示拐点，可以直接包含两边
            curSum = node.val + left + right
            self.sum = max(self.sum, curSum)
            return node.val + max(left, right)

        dfs(root)
        return self.sum
