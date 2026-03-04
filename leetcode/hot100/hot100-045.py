from typing import Optional

# 230 二叉搜索树中第k小的元素
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        return self.dfs(root,k)


    def dfs(self,node: TreeNode,k:int) -> int:
        if not node:
            return None
        lef = self.dfs(node.left,k)
        if lef is not None: # 排除结果是0的影响
            return lef
        self.count += 1
        if self.count == k:
            return node.val
        rig = self.dfs(node.right,k)
        if rig is not None: # 排除结果是0的影响
            return rig
        return None

