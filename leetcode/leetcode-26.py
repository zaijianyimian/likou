from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # se = set()
        # for i in range(len(nums) - 1,-1,-1):
        #     if nums[i] in se:
        #         nums.pop(i)
        #     else:
        #         se.add(nums[i])
        # return len(nums)
        i = 1 # 从1开始方便不遍历第二次。
        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i += 1
        return i

