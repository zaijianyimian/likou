import collections
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dic  = collections.defaultdict(int)
        ans = 0
        i,j = 0,0
        while j < len(nums):
            dic[nums[j]] += 1
            while i < j and dic[nums[j]] > k:
                dic[nums[i]] -= 1
                i += 1
            ans = max(ans,j - i + 1)
            j += 1
        return ans