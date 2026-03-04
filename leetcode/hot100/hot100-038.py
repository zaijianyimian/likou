from typing import Optional

# 226 翻转二叉树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        lef = self.invertTree(root.left)
        rig = self.invertTree(root.right)
        root.left = rig
        root.right = lef
        return root
