from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ans = 0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] > i:
                ans += 1
            else:
                break
        return ans
