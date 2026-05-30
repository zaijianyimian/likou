from typing import List

from sortedcontainers import SortedList


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        m = max(q[1] for q in queries) + 1
        t = [0] * m

        def update(i: int, val: int) -> None:
            while i < m:
                t[i] = max(t[i], val)
                i += i & -i

        def pre_max(i: int) -> int:
            res = 0
            while i:
                res = max(res, t[i])
                i &= i - 1
            return res

        pos = [0] + sorted(q[1] for q in queries if q[0] == 1)
        for i in range(1, len(pos)):
            update(pos[i], pos[i] - pos[i - 1])
        sl = SortedList(pos)
        sl.add(m)  # 哨兵

        ans = []
        for q in reversed(queries):
            x = q[1]
            i = sl.bisect_left(x)
            pre = sl[i - 1]  # x 左侧最近障碍物的位置
            if q[0] == 1:
                sl.discard(x)
                nxt = sl[i]  # x 右侧最近障碍物的位置
                update(nxt, nxt - pre)  # 更新 d[nxt] = nxt - pre
            else:
                # 最大长度要么是 [0,pre] 中的最大 d，要么是 [pre,x] 这一段的长度
                max_gap = max(pre_max(pre), x - pre)
                ans.append(max_gap >= q[2])

        ans.reverse()
        return ans
