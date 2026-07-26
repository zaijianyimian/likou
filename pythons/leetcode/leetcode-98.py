from typing import Optional

# 98 验证二叉搜索树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.Helper(root,float('-inf'),float('inf'))

    def Helper(self,root:TreeNode,lower: int, upper: int) -> bool:
        if not root:
            return True
        if root.val <= lower or root.val >= upper:
            return False
        return self.Helper(root.left,lower,root.val) and self.Helper(root.right,root.val,upper)
