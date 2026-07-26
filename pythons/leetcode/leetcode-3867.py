class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a: int, b: int) -> int:
            if a == b:
                return a
            while b != 0:
                a, b = b, a % b
            return a

        n = len(nums)
        mx = 0
        tmp = [0] * n
        for i in range(n):
            mx = max(mx, nums[i])
            tmp[i] = gcd(mx, nums[i])
        tmp.sort()
        i, j = 0, n - 1
        su = 0
        while i < j:
            su += gcd(tmp[j], tmp[i])
            i += 1
            j -= 1
        return su

s = Solution()
s.gcdSum([3,6,2,8])