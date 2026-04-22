from typing import List

# 763. 划分字母区间
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = dict()
        for i,ch in enumerate(s):
            last[ch] = i
        res = []
        start = 0
        end = 0
        for i,ch in enumerate(s):
            end = max(end,last[ch])
            if i == end:
                res.append(end-start+1)
                start = i+1
        return res
