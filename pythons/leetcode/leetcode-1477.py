from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        l,r = 0,0
        best = [float('inf')] * (len(arr) + 1)
        tmp = 0
        while r < len(arr):
            tmp += arr[r]
            while tmp > target:
                tmp -= arr[l]
                l += 1
            if r > 0:
                best[r] = best[r - 1]

            if tmp == target:
                curlen = r - l + 1
                if l > 0 and best[l - 1] != float('inf'):
                    best[r] = min(best[r], curlen)
                tmp = 0
                l = r + 1


            r += 1

s = Solution()
print(s.minSumOfLengths([7,3,4,7],7))
