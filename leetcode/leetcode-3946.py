from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        gifCnt = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    gifCnt[i] += 1
        dp = [[0] *(budget + 1) for i in range(n + 1)]
        for i in range(1,n + 1):
            idx = i - 1
            price = items[idx][1]
            gift = gifCnt[idx]
            for j in range(1,budget + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= price:

                    dp[i][j] = max(dp[i][j], dp[i - 1][j - price] + gift + 1)
                    dp[i][j] = max(dp[i][j],dp[i][j - price] + 1)
        return dp[n][budget]