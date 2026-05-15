from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans = [0] * 26
        maxCount = 0
        for i in tasks:
            ans[ord(i) - ord('A')] += 1
            maxCount = max(maxCount, ans[ord(i) - ord('A')])
        lens = 0
        for i in ans:
            if i == maxCount:
                lens += 1
        return max((maxCount - 1) * (n + 1) + lens, len(tasks))
