from typing import List


class Solution:
    def lower_bound(self,nums:List[int],target:int) -> int:
        left,right = 0,len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.lower_bound(nums,target)
        if start == len(nums) or nums[start] != target:
            return [-1,-1]
        end = self.lower_bound(nums,target+1) - 1
        return [start,end]

