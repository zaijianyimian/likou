# Definition for a binary tree node.
import collections
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        dic = collections.defaultdict(TreeNode)
        children = set()
        for parent,child,isLeft in descriptions:
            if parent not in dic.keys():
                dic[parent] = TreeNode(parent)
            if child not in dic.keys():
                dic[child] = TreeNode(child)
            if isLeft:
                dic[parent].left = dic[child]
            else:
                dic[parent].right = dic[child]
            children.add(child)
        for parent,child,isLeft in descriptions:
            if parent not in children:
                return dic[parent]

