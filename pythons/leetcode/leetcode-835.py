import collections
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        dic = collections.defaultdict(int)
        n = len(img1)
        ans = 0
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 0:
                    continue
                for x in range(n):
                    for y in range(n):
                        if img2[x][y] == 0:
                            continue
                        dic[(x - i,y - j)] += 1
                        ans = max(ans, dic[(x - i,y - j)])
        return ans

