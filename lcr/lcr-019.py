class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return self.check(i + 1, j, s) or self.check(i, j - 1, s)
            i += 1
            j -= 1
        return True

    def check(self, i: int, j: int, s: str) -> bool:
        while (i < j):
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
