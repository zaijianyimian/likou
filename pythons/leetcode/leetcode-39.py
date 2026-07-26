from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.backtrack(candidates,target,[],ans,0)
        return ans

    def backtrack(self,candidates: List[int],target: int,path: List[int],ans: List[List[int]],index:int):
        if target < 0:
            return
        elif target == 0:
            ans.append(path.copy())
            return
        for i in range(index,len(candidates)):
            path.append(candidates[i])
            self.backtrack(candidates,target-candidates[i],path,ans,i)
            path.pop()
