from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost,res = float('inf'),0
        for price in prices:
            cost = min(cost,price)
            res = max(res,price - cost)
        return res
