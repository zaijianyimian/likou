from typing import List

# 53 最大子数组和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = nums[0]
        ans = pre
        for i in range(1,len(nums)):
            pre = max(pre+nums[i],nums[i])
            ans = max(pre,ans)
        return ans
