from typing import List

# 41 缺失的第一个正数
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr = set(nums)
        for i in range(1,len(nums) + 2):
            if i not in arr:
                return i
        return len(nums) + 1