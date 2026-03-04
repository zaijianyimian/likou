# 5 最长回文串，中心扩散法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ansLeft = ansRight = 0
        for i in range(2 * n - 1):
            l, r = i // 2, (i + 1) // 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > ansRight - ansLeft:
                ansLeft = l + 1
                ansRight = r
        return s[ansLeft:ansRight]
