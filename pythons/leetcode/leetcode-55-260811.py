from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0
        i = 0
        while i <= maxJump:
            maxJump = max(maxJump, i + nums[i])
            i += 1
            if maxJump >= len(nums) - 1:
                return True
        return False
