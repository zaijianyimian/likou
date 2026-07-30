from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for i in range(0,len(strs[0])):
            ma = 0
            for j in range(0,len(strs)):
                if ord(strs[j][i]) >= ma:
                    ma = ord(strs[j][i])
                else:
                    ans += 1
                    break
        return ans