class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        if n < k:
            return 0
        def comb(a,b):
            if b < 0 or b > a:
                return 0
            res = 1
            for i in range(1,b + 1):
                res = res * (a - i + 1) % MOD
                res = res * pow(i,MOD - 2,MOD)% MOD
            return res
        total = comb(n - 1,k - 1)
        odd = 0
        if (n - k) % 2 == 0:
            odd = comb((n + k - 2) // 2, k - 1)
        return (total - odd) % MOD
