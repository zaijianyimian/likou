from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[lo]:  # 左半边有序
                if target >= nums[lo] and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:  # 右半边有序
                if target <= nums[hi] and target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1
