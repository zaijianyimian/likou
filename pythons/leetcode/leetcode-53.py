from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            pre = max(pre +  nums[i] ,nums[i])
            res = max(res,pre)
        return res
