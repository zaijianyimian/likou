from typing import List

# 416. 分割等和子集
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        target = totalSum // 2
        return self.dfs(nums,target)
    def dfs(self,nums: List[int],target: int) -> bool:
        dp = [0] * (target + 1)
        for num in nums:
            for j in range(target,num - 1,-1):
                dp[j] = max(dp[j],dp[j-num] + num)
        return dp[-1] == target
