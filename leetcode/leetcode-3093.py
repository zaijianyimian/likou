from cmath import inf
from typing import List


class Node:
    __slots__ = 'son','minLen','bestInd'
    def __init__(self):
        self.son = [None] * 26
        self.minLen = inf
# 反转后可以转换为前缀树问题
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        ordA = ord('a')
        root = Node()
        for i,s in enumerate(wordsContainer):
            lenS = len(s)
            if lenS < root.minLen:
                root.minLen = lenS
                root.bestInd = i
            cur = root
            for ch in reversed(s):
                c = ord(ch) - ordA
                if cur.son[c] is None:
                    cur.son[c] = Node()
                cur = cur.son[c]
                if lenS < cur.minLen:
                    cur.minLen = lenS
                    cur.bestInd = i
        ans = []
        for s in wordsQuery:
            cur = root
            for ch in reversed(s):
                c = ord(ch) - ordA
                if cur.son[c] is None:
                    break
                cur = cur.son[c]
            ans.append(cur.bestInd)
        return ans