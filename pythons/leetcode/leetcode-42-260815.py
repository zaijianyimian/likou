from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        last = [0] * len(height)
        for i in range(len(height) - 2,-1,-1):
            last[i] = max(last[i + 1],height[i + 1])
        pre = 0
        ans = 0
        for i in range(len(height)):
            tmp = min(pre,last[i])
            if tmp > height[i]:
                ans += tmp - height[i]
            pre = max(pre,height[i])
        return ans
