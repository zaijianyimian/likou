from functools import lru_cache


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def calcNum(num: int) -> int:
            if num <= 0:
                return 0
            digits = list(map(int, str(num)))
            L = len(digits)
            @lru_cache(None)
            def dp(pos,prev,prev_prev,tight):
                # pos 当前位
                # prev 上一位
                # prev_prev上两位
                # tight 是否受上界限制
                if pos == L:
                    return 0
                res = 0
                up = digits[pos] if tight else 9
                for i  in range(0,up + 1):
                    wav = 0
                    if pos >= 2 and pos < L - 1:
                        if prev > prev_prev and prev > i:
                            wav = 1 # 峰
                        elif prev < prev_prev and prev < i:
                            wav = 1
                    res += wav + dp(pos + 1,i,prev,tight and i == up)
                return res
            return dp(0,0,0,True)
        return calcNum(num2) - calcNum(num1 - 1)