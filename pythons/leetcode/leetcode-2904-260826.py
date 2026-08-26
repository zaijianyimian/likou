class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        count = 0
        ans = len(s) + 1
        l, r = 0, 0
        tmp = ''
        while r < len(s):
            if s[r] == '1':
                count += 1
            while count > k:
                if s[l] == '1':
                    count -= 1
                l += 1
            while count == k and s[l] == '0':
                 l += 1
            if count == k:
                cur = s[l : r + 1]
                if (r - l + 1) < ans:
                    ans = r - l + 1
                    tmp = cur
                elif r - l + 1 == ans:
                    tmp = min(tmp, cur)
            r += 1
        return tmp