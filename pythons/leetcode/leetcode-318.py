from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        tmp = [0] * n
        for i in range(n):
            cnt = 0
            for c in words[i]:
                idx = ord(c) - ord("a")
                cnt |= 1 << idx
            tmp[i] = cnt
        ans = 0
        for i in range(n):
            for j in range(i + 1,n):
                if tmp[i] & tmp[j] == 0:
                    ans = max(ans,len(words[i]) * len(words[j]))
        return ans