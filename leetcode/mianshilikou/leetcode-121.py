from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # last = [0 for _ in range(len(prices))]
        # last[len(prices) - 1] = prices[len(prices) - 1]
        # ans = 0
        # for i in range(len(prices) - 2,-1,-1):
        #     last[i] = max(last[i + 1],prices[i])
        # for i in range(len(prices)):
        #     ans = max(ans,last[i] - prices[i])
        # return ans
        ans = 0
        mi = float('inf')
        for i in range(len(prices)):
            mi = min(mi, prices[i])
            ans = max(ans, prices[i] - mi)
        return ans
