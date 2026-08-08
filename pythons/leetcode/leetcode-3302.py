from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m,n = len(word1),len(word2)
        suf = [-1] * (m + 1)
        j = n - 1
        # 找到后缀序列
        for i in range(m - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                suf[i] =  j
                j -= 1
            else:
                suf[i] = suf[i + 1]
        ans = []
        j = 0
        changed = False
        for i in range(m):
            if j == n:
                break
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not changed:
                if j == n - 1 or( suf[i + 1] != -1 and suf[i + 1] <= j + 1):
                    changed = True
                    ans.append(i)
                    j += 1
                else :
                    continue
        return ans if j == n else []
