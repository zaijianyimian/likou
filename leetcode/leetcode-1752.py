from typing import List

# 最多只有一个递减点，前后要衔接
class Solution:
    def check(self, nums: List[int]) -> bool:
        nums.append(nums[0])
        ans = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i - 1]:
                ans += 1
        return ans <= 1
