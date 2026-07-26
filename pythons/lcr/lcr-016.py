class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l,r = 0,0
        map = [0] * 128
        """这里没限制全为小写字符，所以直接用最大ASCII码来表示"""
        ans = 0
        while r < n:
            map[ord(s[r])] += 1
            while map[ord(s[r])] > 1 and l <= r:
                map[ord(s[l])] -= 1
                l += 1
            ans = max(ans, r-l+1)
            r += 1
        return ans