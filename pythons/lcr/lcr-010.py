from collections import defaultdict
from typing import List

# 前缀和 + hash表
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        pre = 0
        dic = defaultdict(int)
        dic[0] = 1
        for i in range(len(nums)):
            pre += nums[i]
            ans += dic[pre - k]
            dic[pre] += 1
        return ans
