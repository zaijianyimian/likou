from typing import List
import heapq


# 215. 数组中的第K个最大元素
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in nums:
            heapq.heappush(heap, i)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
