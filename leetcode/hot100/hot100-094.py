from typing import List

# 64 最小路径和
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        dp[m - 1][n - 1] = grid[m - 1][n - 1]
        for i in range(m - 1,-1,-1):
            for j in range(n - 1,-1,-1):
                if i == m - 1 and j == n - 1:
                    continue
                else:
                    if  i + 1 < m and j + 1 < n:
                        dp[i][j] = min(dp[i + 1][j],dp[i][j + 1]) + grid[i][j]
                    elif i + 1 < m:
                        dp[i][j] = dp[i + 1][j] + grid[i][j]
                    elif j + 1 < n:
                        dp[i][j] = dp[i][j + 1] + grid[i][j]
        return dp[0][0]