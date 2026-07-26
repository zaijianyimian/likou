from typing import Counter

# 76 最小覆盖子串
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cntS = Counter()
        cntT = Counter(t)
        ansL,ansR = -1,len(s)
        left = 0
        for right,c in enumerate(s):
            cntS[c] += 1
            while cntS >= cntT:
                if right - left < ansR - ansL:
                    ansL, ansR = left, right
                cntS[s[left]] -= 1
                left += 1
        return "" if ansL < 0 else s[ansL:ansR+1]