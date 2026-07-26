from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        maxJump = 0
        curJump = 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            curJump = max(curJump, i + nums[i])
            if maxJump == i:
                ans += 1
                maxJump = curJump
            if maxJump >= len(nums) - 1:
                return ans
        return -1
s = Solution()
print(s.jump([1,2,3]))

