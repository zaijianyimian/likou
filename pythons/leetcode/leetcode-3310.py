from collections import defaultdict
from typing import List


class Solution:
    def remainingMethods(
        self,
        n: int,
        k: int,
        invocations: List[List[int]]
    ) -> List[int]:

        graph = defaultdict(list)

        for a,b in invocations:
            graph[a].append(b)


        # 找k能影响的方法
        bad = set([k])
        stack = [k]

        while stack:
            node = stack.pop()

            for nxt in graph[node]:
                if nxt not in bad:
                    bad.add(nxt)
                    stack.append(nxt)


        # 检查外部调用
        for a,b in invocations:
            if a not in bad and b in bad:
                return list(range(n))


        return [
            i for i in range(n)
            if i not in bad
        ]