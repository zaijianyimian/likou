# Definition for singly-linked list.
import collections
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        dummy = ListNode()
        pre = slow
        while pre:
            nxt = pre.next
            pre.next = dummy.next
            dummy.next = pre
            pre = nxt
        p = head
        q = dummy.next
        ans = 0
        while p and q:
            tmp = p.val + q.val
            if tmp > ans:
                ans = tmp
            p = p.next
            q = q.next
        return ans

