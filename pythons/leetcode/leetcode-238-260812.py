from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        last = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            last[i] = last[i+1] * nums[i+1]
        pre = 1
        for i in range(1,len(nums)):
            pre *= nums[i - 1]
            last[i] = pre * last[i]
        return last
