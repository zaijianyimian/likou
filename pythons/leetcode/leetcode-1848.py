from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                curInd = abs(i - start)
                if curInd < ans:
                    ans = curInd
        return ans