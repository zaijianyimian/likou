from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lef,rig = -1,len(nums)-1
        while lef + 1 < rig:
            mid = (lef + rig) // 2
            if nums[mid] == nums[rig]:
                rig -= 1
            elif nums[mid] < nums[rig]:
                rig = mid
            else:
                lef = mid
        return nums[rig]