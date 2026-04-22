import collections
from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ans = s = 0
        dic = collections.defaultdict(int)
        for i,x in enumerate(nums):
            s += x
            dic[x] += 1
            left = i - k + 1
            if left < 0:
                continue
            if len(dic) >= m:
                ans = max(ans,s)
            s -= nums[left]
            dic[nums[left]] -= 1
            if dic[nums[left]] == 0:
                del dic[nums[left]]
        return ans
