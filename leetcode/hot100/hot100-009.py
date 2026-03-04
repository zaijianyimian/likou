from typing import List, Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cntP = Counter(p) # 记录p中字符出现的次数
        cntS = Counter() # 窗口中字符出现的次数
        if len(s) < len(p):
            return []
        ans = []
        for i in range(len(s)):
            cntS[s[i]] += 1
            left = i - len(p) + 1 # 窗口左边界
            if left < 0:
                continue
            if cntS == cntP:
                ans.append(left)
            cntS[s[left]] -= 1
        return ans