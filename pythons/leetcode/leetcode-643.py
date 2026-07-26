from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = 0
        su = sum(nums[:k])
        ans = su / k
        for i in range(k,len(nums)):
            su += nums[i] - nums[i-k]
            ans = max(ans, su / k)
        return ans
