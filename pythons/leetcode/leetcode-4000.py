class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s > (n * 9):
            return -1
        ans = [0] * n
        for i in range(0,n):
            if s > 9:
                ans[i] = 9
                s -= 9
            else:
                ans[i] = s
                break
        return int(''.join(map(str, ans)))