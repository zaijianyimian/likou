from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        ans = strs[0]
        for i in range(1,len(strs)):
            if len(ans) == 0:
                return ""
            ind = min(len(strs[i]),len(ans))
            ans = ans[:ind]
            for j in range(ind):
                if strs[i][j] == ans[j]:
                    continue
                else:
                    ans = ans[:j]
                    break
        return ans



