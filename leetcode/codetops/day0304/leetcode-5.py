class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ansleft = ansright = 0
        # 为什么这里要循环到2 * n - 1
        # 间隙中心+字符中心
        for i in range(2 * n - 1):
            l,r = i // 2,(i + 1) // 2
            while l > 0 and r < n and s[l] == s[r]:
                l -=1
                r +=1
            if r - l - 1 > ansright - ansleft:
                ansleft = l + 1
                ansright = r
        return s[ansleft:ansright]