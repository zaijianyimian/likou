from typing import List

# 152. 乘积最大子数组 同时维护两个dp数组
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [(float)] * len(nums)
        res = nums[0]
        max_dp = [0] * len(nums)
        min_dp = [0] * len(nums)

        max_dp[0] = min_dp[0] = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > 0:
                max_dp[i] = max(nums[i], nums[i] * max_dp[i - 1])
                min_dp[i] = min(nums[i], nums[i] * min_dp[i - 1])
            else:
                max_dp[i] = max(nums[i], nums[i] * min_dp[i - 1])
                min_dp[i] = min(nums[i], nums[i] * max_dp[i - 1])
            res = max(res, max_dp[i])
        return res