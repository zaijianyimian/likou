from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        se = set()
        for i in arr1:
            temp = str(i)
            for j in range(len(temp)):
                se.add(temp[:j+1])
        ans = 0
        for i in arr2:
            temp = str(i)
            for j in range(len(temp)):
                if temp[:j+1] in se:
                    ans = max(ans, j+1)
        return ans