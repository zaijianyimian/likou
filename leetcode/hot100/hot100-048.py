from typing import List, Optional

# 105 从前序和中序遍历序列构造二叉树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0]) # 确定根节点
        mid = inorder.index(preorder[0]) # 确定根节点在中序遍历中的位置
        root.left = self.buildTree(preorder[1:mid + 1],inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:],inorder[mid + 1:])
        return root

