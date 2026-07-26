from itertools import accumulate
from math import inf
from typing import List


# 右边小于左边，可以往右边跳 nums[j] < nums[i] j > i
# 左边大于右边，可以往左边跳，nums[j] > nums[i] j < i

# 就是先跳到右边最小的，再跳到左边最大的
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preMax = list(accumulate(nums,max))
        ans = [0] * n
        sufMin = inf
        for i in range(n - 1, -1, -1):
            ans[i] = preMax[i] if preMax[i] <= sufMin else ans[i + 1]
            sufMin = min(sufMin, nums[i])
        return ans
