from typing import List


class Solution:
    def lexicographicallySmallestArray(
        self, nums: List[int], limit: int
    ) -> List[int]:

        n = len(nums)

        # 按 nums[i] 的值从小到大排列下标
        #
        # 例如：
        # nums = [5, 1, 3]
        # pos = [1, 2, 0]
        #
        # 因为：
        # nums[1] = 1
        # nums[2] = 3
        # nums[0] = 5
        pos = sorted(range(n), key=lambda i: nums[i])

        # 最终答案
        ans = [0] * n

        # 当前连通组在 pos 中的起点
        start = 0

        # 按值从小到大遍历
        for i, p in enumerate(pos):

            # 如果：
            #
            # 1. 已经是最后一个元素
            #
            # 或
            #
            # 2. 当前值和下一个值的差 > limit
            #
            # 那么说明当前交换组到这里结束
            if (
                i == n - 1
                or nums[pos[i + 1]] - nums[p] > limit
            ):

                # 当前交换组中的所有原数组下标
                #
                # 然后按照下标从小到大排序
                sub_pos = sorted(pos[start:i + 1])

                # 当前组中的值已经按照升序排列：
                #
                # nums[pos[start]]
                # nums[pos[start + 1]]
                # ...
                #
                # 当前组中的位置 sub_pos 也按升序排列。
                #
                # 为了让字典序最小：
                #
                # 最小位置 <- 最小值
                # 第二小位置 <- 第二小值
                # ...
                for j, q in enumerate(sub_pos):
                    ans[q] = nums[pos[start + j]]

                # 下一组从 i + 1 开始
                start = i + 1

        return ans