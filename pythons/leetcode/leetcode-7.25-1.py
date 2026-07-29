class Solution:
    def maximumNumberOfPrimes(self, low: int, high: int) -> int:
        nums = [0] * (high + 1)
        nums[2] = 1
        for i in range(2, high + 1):
            if nums[i] == 0:
                nums[i] = 1
            tmp = i
            while tmp + i <= high:
                tmp += i
                nums[tmp] += 1
        mx, ind = 0, 0
        for i in range(low, high + 1):
            if nums[i] >= mx:
                mx = nums[i]
                ind = i
        return ind


s = Solution()
print(s.maximumNumberOfPrimes(8,11))


