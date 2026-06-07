class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        n = len(s1)
        ans = []
        l, r = 0, 0
        for r in range(n):
            cnt1[ord(s1[r]) - ord('a')] += 1
            cnt2[ord(s2[r]) - ord('a')] += 1
        if cnt1 == cnt2:
            return True
        r += 1
        while r < len(s2):
            cnt2[ord(s2[r]) - ord('a')] += 1
            cnt2[ord(s2[l]) - ord('a')] -= 1
            if cnt1 == cnt2:
                ans.append(l)
            l += 1
            r += 1
        return False
