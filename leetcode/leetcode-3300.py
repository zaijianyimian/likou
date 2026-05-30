from cmath import inf
from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        mi = inf
        for i in range(len(nums)):
            s = str(nums[i])
            tmp = 0
            for j in s:
                 num = int(j)
                 tmp += num
            mi = min(mi, tmp)
        return int(mi)