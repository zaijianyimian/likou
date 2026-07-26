from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        arr = ['a'] * 26
        c = 'z'
        for i in range(len(arr)):
            arr[i] = c
            c = chr(ord(c) - 1)
        for s in  words:
            tmp = 0
            for ch in s:
                tmp += weights[ord(ch) - ord('a')]
            tmp %= 26
            ans.append(arr[tmp])
        return ''.join(ans)