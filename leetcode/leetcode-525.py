import collections
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLen = 0
        n = len(nums)
        pre = 0
        dic = {0:-1}
        # key: 前缀和
        # value: 这个前缀和第一次出现的位置
        for i in range(n):
            pre += 1 if nums[i] == 1 else -1
            if pre in dic:
                maxLen = max(maxLen,i - dic[pre])
            else:
                dic[pre] = i
        return maxLen