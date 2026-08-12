from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort(reverse=True)
        ans = 0
        for ans in range(n):
            if citations[ans] > ans:
                ans += 1
            else:
                break
        return ans
