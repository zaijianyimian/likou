from random import randint
from typing import List

# 这段代码有大问题，明天再改
class Solution:
    def partition(self,nums:List[int],left: int,right: int) -> int:
        i = randint(left,right)
        pivot = nums[i]
        nums[i],nums[left] = nums[left],nums[i]
        i,j = left + 1,right
        while True:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i >= j:
                break
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
        return j

    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(left: int, right: int) -> None:
            if left >= right:
                return
            # 检查是否已经有序
            ordered = True
            for i in range(left, right):
                if nums[i] > nums[i + 1]:
                    ordered = False
                    break
            if ordered:
                return
            i = self.partition(nums, left, right)
            quickSort(left, i - 1)
            quickSort(i + 1, right)

        quickSort(0, len(nums) - 1)
        return nums


