from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            res = 1
            # 向右跳
            for j in range(i + 1,min(i +d + 1,n)):
                if arr[j] >= arr[i]:
                    break
                res = max(res,dfs(j) + 1)
            # 向左跳
            for k in range(i - 1,max(i - d - 1,-1),-1):
                if arr[k] >= arr[i]:
                    break
                res = max(res,dfs(k) + 1)
            memo[i] = res
            return res
        return max(dfs(i) for i in range(n))