class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        tmp = (brightness + 2) // 3
        intervals.sort(key=lambda x: (x[0], x[1]))
        sumIntervals = 0
        # 合并区间
        left,right = 0,-1
        for l,r in intervals:
            if l <= right:
                right = max(right, r)
            else:
                sumIntervals += right - left + 1
                left,right = l,r
        sumIntervals += right - left + 1
        return sumIntervals * tmp