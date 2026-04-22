from functools import cache
from typing import List
from math import inf


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        @cache
        def dfs(i: int, j: int, k: int) -> int:
            if i < 0 or j < 0:
                return -inf # 避免越界
            x = coins[i][j]
            if i == 0 and j == 0:
                return max(x, 0) if k else x
            res = max(dfs(i - 1, j, k), dfs(i, j - 1, k)) + x  # 选
            if k and x < 0:
                res = max(res, dfs(i - 1, j, k - 1), dfs(i, j - 1, k - 1))  # 不选
            return res

        return dfs(len(coins) - 1, len(coins[0]) - 1, 2)
