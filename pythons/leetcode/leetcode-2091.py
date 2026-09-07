from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        mi,ma = min(nums),max(nums)
        indmi,indma = nums.index(mi),nums.index(ma)
        left = min(indmi, indma)
        right = max(indmi, indma)
        return min(right + 1,n - left,left + 1 + n - right)
