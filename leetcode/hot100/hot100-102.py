from typing import List

# 287 寻找重复数
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        head = 0
        while head != slow:
            head = nums[head]
            slow = nums[slow]
        return slow
