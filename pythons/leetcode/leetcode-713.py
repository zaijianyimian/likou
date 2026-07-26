from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 0:
            return 0
        left  = 0
        ans = 0
        tmp = 1
        for i in range(0, len(nums)):
            tmp *= nums[i]
            while left <= i and tmp >= k:
                tmp /= nums[left]
                left += 1
            ans += i - left  + 1 if i >= left else 0
        return ans