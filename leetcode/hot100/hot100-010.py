from collections import defaultdict
from typing import List

# 560 和为k的子数组，不是子序列
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        dict = defaultdict(int)
        sum = 0
        dict[0] = 1 # dict【0】必须初始化为1，否则当出现num[i] == k时获取到dict[sum-k]是0，或者根本不在dict内
        for i in nums:
            sum += i
            if sum - k in dict:
                count += dict[sum - k]
            dict[sum] += 1
        return count
