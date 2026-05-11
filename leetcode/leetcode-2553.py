from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            tmp = str(i)
            for j in tmp:
                ans.append(int(j))
        return ans