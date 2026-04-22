class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(map(str,s.split()))
        return " ".join(arr[::-1])