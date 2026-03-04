from typing import List

# 136 只出现一次的数字
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        return ans
