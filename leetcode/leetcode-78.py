from typing import List

# 78 子集
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        self.backtrack(nums,[],res)
        return res
    def backtrack(self,nums:List[int],path:List[int],res:List[List[int]]):
        res.append(path[:])
        for i in range(len(nums)):
            if nums[i] in path:
                continue
            path.append(nums[i])
            self.backtrack(nums[i+1:],path,res)
            path.pop()


