import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            nodes = []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                # 这里可以不用判断node.left,node.right
                if node:
                    nodes.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if nodes:
                res.append(nodes)
        return res