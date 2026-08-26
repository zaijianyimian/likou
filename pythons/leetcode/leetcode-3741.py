from typing import Counter, List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        def f(nums: list, x: int) -> int:
            return -1 if x in nums else x

        if k == len(nums):
            return max(nums)
        if k == 1:
            ans = -1
            for x, c in Counter(nums).items():
                if c == 1:
                    ans = max(ans, x)
            return ans
        return max(f(nums[1:], nums[0]), f(nums[:-1], nums[-1]))
