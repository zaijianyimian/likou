from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ans = 0
        allZero = True
        for i in nums:
            ans ^= i
            if i != 0:
                allZero = False
        if ans != 0:
            return len(nums)
        return len(nums) -  1 if not allZero else len(nums)
