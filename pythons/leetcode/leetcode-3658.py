class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0
        for i in range(2 * n):
            if i % 2 == 0:
                sumEven += i
            else:
                sumOdd += i
        for i in range(min(sumEven,sumOdd),0,-1):
            if sumEven % i == 0 and sumOdd % i == 0:
                return  i
        return -1
s = Solution()
print(s.gcdOfOddEvenSums(4))
