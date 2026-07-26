from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # for i in range(len(nums) - 1,-1,-1): 正序遍历会导致序号增加，但是删除元素会导致序号减少
        #     if nums[i] == val:
        #         nums.pop(i)
        # return len(nums)
        i,j = 0,len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i],nums[j] = nums[j],nums[i]
                j -= 1
            else:
                i += 1
        return i