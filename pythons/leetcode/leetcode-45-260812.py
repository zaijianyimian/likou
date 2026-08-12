from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        ans = 0
        maxJump = 0
        curJump = 0
        for i in range(len(nums)):
            maxJump = max(maxJump, i + nums[i])
            if i == curJump:
                ans += 1
                curJump = maxJump
            if curJump >= len(nums) - 1:
                return ans
        return ans
