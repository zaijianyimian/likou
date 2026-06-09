class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        sum = 0
        for x in range(max(0,n - k),n + k + 1):
            if n & x == 0:
                sum += x
        return sum
n,k = 2,3
s = Solution()
s.sumOfGoodIntegers(n,k)