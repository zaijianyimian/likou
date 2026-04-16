import collections
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
       # n = len(nums)
       # k = k % n
       # queue = collections.deque(nums)
       # for i in range(k):
       #     queue.appendleft(queue.pop())
       # nums[:] = list(queue)
       k = k % len(nums)
       if k > 0:
        nums[:] = nums[-k:] + nums[:len(nums) - k]
