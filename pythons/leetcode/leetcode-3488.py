from collections import defaultdict
from typing import List
import sys

input =  sys.stdin.readline

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        posDict = defaultdict(list)
        for i,num in enumerate(nums):
            posDict[num].append(i)
        minDist = [-1] * n
        for num,indices in posDict.items():
            k = len(indices)
            if k <= 1:
                continue
            for i in range(k):
                curInd = indices[i]
                leftInd = indices[(i - 1 + k) % k]
                rigInd = indices[(i + 1) % k]
                distLeft = min(abs(curInd - leftInd),n - abs(curInd - leftInd))
                distRig = min(abs(curInd - rigInd),n - abs(curInd - rigInd))
                minDist[curInd] = min(distLeft,distRig)
        return [minDist[query] for query in queries]

if __name__=="__main__":
    nums = list(map(int,input().split()))
    queries = list(map(int,input().split()))
    print(Solution().solveQueries(nums,queries))