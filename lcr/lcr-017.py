class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        need = [0] * 128
        window = [0] * 128
        needCount = 0
        for ch in t:
            idx = ord(ch)
            if need[idx] == 0:
                needCount += 1
            need[idx] += 1
        l = 0
        valid = 0
        start = 0
        minLen = float("inf")
        for r in range(len(s)):
            c = ord(s[r])
            window[c] += 1
            if need[c] > 0 and window[c] == need[c]:
                valid += 1
            while valid == needCount:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    start = l
                d = ord(s[l])
                if need[d] > 0 and window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
                l += 1
        if minLen == float("inf"):
            return ""
        return s[start: start + minLen]
