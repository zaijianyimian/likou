from functools import cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suf = [0] * (n + 1)
        for i in range(n - 1,- 1,- 1):
            # 后缀和，方便计算当前玩家的得分
            suf[i] = piles[i] + suf[i + 1]
        @cache
        def dfs(i,M):
            # 递归边界，剩余棋子数量小于等于2M，直接返回当前缀和
            if i + 2 * M >= n:
                return suf[i]
            # 递归计算当前玩家的得分
            ans = 0
            # 枚举当前玩家取的棋子数量
            for x in range(1,2 * M + 1):
                # 对手的得分，当前玩家的得分就是当前缀和减去对手的得分
                opponent = dfs(i + x,max(M,x))
                current = suf[i] - opponent
                ans = max(ans,current)
            return ans
        return dfs(0,1)