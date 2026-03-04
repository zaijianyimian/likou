from typing import List

# 189. 旋转数组
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        # 从后往前数-k个到最后的数先加入数组，然后从0到-k的数加入数组
        # nums[:] 表示原地修改，如果直接修改nums=则会创建新列表，而不是原地修改
