from typing import List

#  198. 打家劫舍
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev2 = prev = 0
        for i in nums:
            current = max(prev,prev2 + i)
            prev2 = prev
            prev = current
        return prev