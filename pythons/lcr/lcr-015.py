from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        n = len(p)
        ans = []
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        l, r = 0, 0
        for r in range(n):
            cnt1[ord(p[r]) - ord('a')] += 1
            cnt2[ord(s[r]) - ord('a')] += 1
        r += 1
        if cnt1 == cnt2:
            ans.append(l)
        while r < len(s):
            cnt2[ord(s[r]) - ord('a')] += 1
            cnt2[ord(s[l]) - ord('a')] -= 1
            l += 1
            r += 1
            """这里加减顺序不能反"""
            if cnt1 == cnt2:
                ans.append(l)
        return ans
