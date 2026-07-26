from typing import List, Optional

# 108 将有序数组转化为二叉搜索树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.dfs(nums,0,len(nums) - 1)
    def dfs(self,nums: List[int],left: int,right: int) -> TreeNode:
        if left > right:
            return None
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.dfs(nums,left,mid - 1)
        node.right = self.dfs(nums,mid + 1,right)
        return node
