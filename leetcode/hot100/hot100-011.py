import collections
from collections import deque
from typing import List

# 239. 滑动窗口最大值
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []
        queue = collections.deque()
        res = []
        for i in range(k): # 形成窗口前
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
        res.append(queue[0])
        for i in range(k, len(nums)): # 形成窗口后
            if queue[0] == nums[i - k]:
                queue.popleft()
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            res.append(queue[0])
        return res


