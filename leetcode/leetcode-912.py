from random import randint
from typing import List

# 这段代码有大问题，明天再改
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(left: int, right: int) -> None:
            if left >= right:
                return
            i,j = left,right
            x = (left + right) // 2
            while i < j:
                while nums[i] < nums[x]:
                    i += 1
                while nums[j] > nums[x]:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            quickSort(left, j)
            quickSort(j + 1, right)

        quickSort(0, len(nums) - 1)
        return nums


