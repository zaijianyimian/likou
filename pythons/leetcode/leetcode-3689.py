from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        ma = max(nums)
        mi = min(nums)
        return (ma - mi) * k