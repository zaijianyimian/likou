from collections import defaultdict
from typing import List, Counter
import heapq

# 347. 前 K 个高频元素
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for val,freq in count.items():
            heapq.heappush(heap,(freq,val))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res



