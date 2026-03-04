from typing import Optional, List

# 94 中序遍历二叉树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        return self.dfs(root,res)

    def dfs(self,node: Optional[TreeNode],res : List[int]) -> List[int]:
        if not node:
            return res
        self.dfs(node.left,res)
        res.append(node.val)
        self.dfs(node.right,res)
        return res