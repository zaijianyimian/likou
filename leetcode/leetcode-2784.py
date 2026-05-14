from collections import defaultdict
from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        a = []
        for i in range(n - 1):
            a.append(i + 1)
        a.append(n - 1)
        return a == nums
