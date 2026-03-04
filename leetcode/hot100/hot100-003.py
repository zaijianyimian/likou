from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        dic = set(nums)
        for num in nums:
            if num - 1 not in dic:
                cur = num
                count = 1
                while cur + 1 in dic:
                    cur += 1
                    count += 1
                    dic.remove(cur)
                res = max(res, count)
        return res
