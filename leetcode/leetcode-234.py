from typing import Optional

# 234 回文链表 直接复制到数组实现
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val = []
        while head:
            val.append(head.val)
            head = head.next
        return val == val[::-1]
