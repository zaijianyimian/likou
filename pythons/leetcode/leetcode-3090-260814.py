class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = [0] * 26
        ans = 0
        l, r = 0, 0
        while r < len(s):
            count[ord(s[r]) - ord('a')] += 1

            while count[ord(s[r]) - ord('a')] > 2:
                count[ord(s[l]) - ord('a')] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans
