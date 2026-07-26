from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        ans1 = nums[0] * nums[1] * nums[-1]
        ans2 = nums[-1] * nums[-2] * nums[-3]
        return ans2 if ans2 > ans1 else ans1
