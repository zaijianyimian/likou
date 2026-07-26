from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        su = sum(nums)
        pre = 0
        for i in range(n):
            if su - nums[i] - pre == pre:
                return i
            pre += nums[i]
        return -1
