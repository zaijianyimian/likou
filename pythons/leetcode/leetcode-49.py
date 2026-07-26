from typing import List

# 字母异位词分组 leetcode-49
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for s in strs:
            key = tuple(sorted(s))
            if key not in dic:
                lis = []
            else:
                lis = dic[key]
            lis.append(s)
            dic[key] = lis
        res = [dic[key] for key in dic]
        return res
