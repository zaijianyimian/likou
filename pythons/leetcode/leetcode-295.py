import heapq


class MedianFinder:
    # 小顶堆+大顶堆
    def __init__(self):
        self.queMin = []
        self.queMax = []
    def addNum(self, num: int) -> None:
        if not self.queMin or num <= -self.queMin[0]:
            heapq.heappush(self.queMin, -num)
            if len(self.queMin) - 1 > len(self.queMax):
                heapq.heappush(self.queMax,-heapq.heappop(self.queMin))
        else:
            heapq.heappush(self.queMax, num)
            if len(self.queMax) > len(self.queMin):
                heapq.heappush(self.queMin, -heapq.heappop(self.queMax))
    def findMedian(self) -> float:
        if len(self.queMin) > len(self.queMax):
            return -self.queMin[0]
        else:
            return (-self.queMin[0] + self.queMax[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()