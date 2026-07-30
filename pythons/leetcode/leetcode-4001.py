class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        m,n = len(series1),len(series2)
        i,j = 0,0
        ans = []
        while i < m and j < n:
            tmp = [0,0]
            tmp[1] = series1[i][1] + series2[j][1]
            if series1[i][0] < series2[j][0]:
                tmp[0] = series1[i][0]
                i += 1
            elif series1[i][0] > series2[j][0]:
                tmp[0] = series2[j][0]
                j += 1
            else:
                tmp[0] = series1[i][0]
                i += 1
                j += 1
            ans.append(tmp)
        if i != m:
            ans.extend(series1[i:])
        elif j != n:
            ans.extend(series2[j:])
        return ans