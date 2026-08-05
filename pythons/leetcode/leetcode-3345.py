class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(10):
            num = n
            tmp = 1
            while num > 0:
                tmp *= num % 10
                num //= 10
            if tmp % t == 0:
                return n
            n += 1
        return -1