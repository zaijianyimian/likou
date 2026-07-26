from typing import List

# 22 括号生成
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        if n == 0:
            return ans
        self.backtrack(ans,n,0,0,'')
        return ans
    def backtrack(self,ans: List[str],n: int,left: int,right: int,path: str) -> None:
        if left == n and right == n:
            ans.append(path)
            return
        if left < n:
            self.backtrack(ans,n,left+1,right,path+'(')
        if right < left:
            self.backtrack(ans,n,left,right+1,path+')')