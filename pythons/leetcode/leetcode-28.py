class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        def buildNext(pattern:str):
            m = len(pattern)
            nextArr = [0] * m
            j = 0
            for i in range(1,m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = nextArr[j-1]
                if pattern[i] == pattern[j]:
                    j += 1
                nextArr[i] = j
            return nextArr
        m = len(haystack)
        n = len(needle)
        if n > m:
            return -1
        nextArr = buildNext(needle)
        j = 0
        for i in range(m):
            while j > 0 and haystack[i] != needle[j]:
                j = nextArr[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == n:
                return i - n + 1
        return -1