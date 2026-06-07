class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        m = n & (n >> 1)
        return m > 0 and m & (m - 1) == 0