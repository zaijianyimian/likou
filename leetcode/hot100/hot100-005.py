from typing import List

# 11 盛最多水的容器
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = min(height[l], height[r]) * (l - r)
        while l <= r:
            cur = min(height[l], height[r])
            wid = r - l
            res = max(res,cur * wid)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

