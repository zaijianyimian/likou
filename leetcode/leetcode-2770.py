from math import inf
from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        if len(nums) < 2:
            return 0
        n = len(nums)
        dp = [-inf] * n
        dp[0] = 0
        for i in range(1,n):
            for j in range(0,i):
                if abs(nums[i]-nums[j]) <= target:
                    dp[i] = max(dp[i],dp[j]+1)
        return dp[-1] if dp[-1] != -inf else -1
