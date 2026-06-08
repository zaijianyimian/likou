from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        lef = []
        rig = []
        mid = []
        j = 0
        for i in range(n):
            if nums[i] < pivot:
                lef.append(nums[i])
            elif nums[i] > pivot:
                rig.append(nums[i])
            else:
                mid.append(nums[i])
        return lef + mid + rig