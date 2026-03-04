from typing import List

# 121 买卖股票的最佳时机
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost,ans = float('inf'),0
        for price in prices:
            cost = min(cost,price)
            ans = max(ans,price-cost)
        return ans