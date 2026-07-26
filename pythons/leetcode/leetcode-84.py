from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 添加哨兵节点
        heights.insert(0,0)
        heights.append(0)

        stack = [0]
        ans = 0
        for i in range(1,len(heights)):
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            elif heights[i] == heights[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)
        return ans