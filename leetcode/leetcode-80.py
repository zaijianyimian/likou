from ast import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # stack = 2 # 利用栈来判断当前元素和他的前两个是否相等
        # for i in range(2,len(nums)):
        #     if nums[i] != nums[stack-2]:
        #         nums[stack] = nums[i]
        #         stack += 1
        # return min(len(nums),stack)
        i = 2
        for j in range(2,len(nums)):
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        return i

