from typing import List

# 56. 合并区间
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        tmp = intervals[0]
        for i in intervals:
            if i[0] <= tmp[1]:
                tmp[1] = max(tmp[1], i[1])
            else:
                res.append(tmp)
                tmp = i
        res.append(tmp)
        return res
