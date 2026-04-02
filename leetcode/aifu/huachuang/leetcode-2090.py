from typing import List

# 半径为k的子数组
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * len(nums)
        s = 0
        for i,x in enumerate(nums):
            s += x
            if i < 2 * k:
                continue
            ans[i - k] = s // (2 * k + 1)
            s -= nums[i - 2 * k]
        return ans
