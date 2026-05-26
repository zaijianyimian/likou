class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        se = set(word)
        for c in range(ord('a'), ord('z') + 1):
            lo = chr(c)
            up = lo.upper()
            if lo in se and up in se:
                ans += 1
        return ans