from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        pre = [1] * len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                pre[i] = pre[i-1] + 1
        last = [1] * len(ratings)
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                last[i] = max(last[i], last[i+1] + 1)
        for i in range(len(ratings)):
            pre[i] = max(pre[i], last[i])
        return sum(pre)
