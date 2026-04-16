from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]* len(nums)
        last = [1] * len(nums)
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            last[i] = last[i+1] * nums[i+1]
        for i in range(len(nums)):
            nums[i] = pre[i] * last[i]
        return nums
