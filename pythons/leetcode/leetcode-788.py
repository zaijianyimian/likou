from tldextract import cache

DIFFS = (0, 0, 1, -1, -1, 1, 1, -1, 0, 1)
class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = str(n)
        @cache
        def f(i : int,hasDiff: bool,isLimit: bool) -> int:
            if i == len(s):
                return hasDiff
            res = 0
            up = int(s[i]) if isLimit else 9
            for d in range(0,up + 1):
                if DIFFS[d] != -1:
                    res += f(i + 1,hasDiff or DIFFS[d],isLimit and d == up)
            return res
        return f(0,False,True)