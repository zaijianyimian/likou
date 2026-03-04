from typing import Optional

# 114 二叉树展开为链表
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.res = []
        self.dfs(root)
        for i in range(len(self.res)):
            if i == len(self.res) - 1:
                self.res[i].left = None
                self.res[i].right = None
            else:
                self.res[i].left = None
                self.res[i].right = self.res[i+1]


    def dfs(self,node:Optional[TreeNode]): # 记录先序遍历结果
        if not node:
            return
        self.res.append(node)
        self.dfs(node.left)
        self.dfs(node.right)