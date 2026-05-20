from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        p = q = 0
        for a,b in zip(A,B):
            p |= 1 << a
            q |= 1 << b
            res.append((p & q).bit_count())
        return  res
if __name__ == '__main__':
    A = [1,3,2,4]
    B = [3,1,2,4]
    print(Solution().findThePrefixCommonArray(A, B))