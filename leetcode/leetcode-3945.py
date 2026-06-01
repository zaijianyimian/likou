class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        ans = [0] * 10
        while n > 0:
            tmp = n % 10
            ans[tmp] += 1
            n //= 10
        res = 0
        for i in range(len(ans)):
            res += ans[i] * i
        return res