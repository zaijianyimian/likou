class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord("a")] += 1
        half = []
        mid = ''
        for i in range(26):
            if cnt[i] >= 2:
                half.append(chr(i + ord("a")) * (cnt[i] // 2))
            if cnt[i] %2 == 1:
                mid = chr(ord("a") + i)
        left = ''.join(half)
        right = left[::-1]
        return left + mid + right

