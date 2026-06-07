from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        ans = 0
        flag = 1
        for i in range(len(cost)):
            if flag != 0:
                ans += cost[i]
            flag += 1
            flag = flag % 3
        return ans