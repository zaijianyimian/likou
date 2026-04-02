from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        avg = 0
        su = sum(arr[:k - 1])
        for i in range(k - 1, len(arr)):
            su += arr[i]
            avg = su / k
            if avg >= threshold:
                ans += 1
            su -= arr[i - k + 1]
        return ans
        