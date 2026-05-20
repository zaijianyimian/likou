from math import inf
from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        se = set(nums1)
        ans = inf
        for i in nums2:
            if i in se:
                if i < ans:
                    ans = i
        return ans if ans != inf else -1
