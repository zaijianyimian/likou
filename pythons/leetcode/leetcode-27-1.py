from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tail = len(nums) - 1
        while tail >= 0 and nums[tail] == val:
            tail -= 1
        i = 0
        while i <= tail :
            if nums[i] == val:
                nums[i],nums[tail] = nums[tail],nums[i]
                tail -= 1
            else:
                i += 1
        return i
