from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        sum = 0
        maxLeft = 0
        maxRight = [0] * len(height)
        for i in range(len(height) - 2,-1,-1):
            maxRight[i] = max(maxRight[i + 1],height[i + 1])
        for i in range(1,len(height) - 1):
            maxLeft = max(maxLeft,height[i - 1])
            minHeight = min(maxLeft,maxRight[i])
            if minHeight > height[i]:
                sum += minHeight - height[i]
        return sum