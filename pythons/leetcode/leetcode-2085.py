# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow = head
        fast = head
        pre = dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            pre = pre.next
        pre.next = slow.next
        slow.next = None
        return dummy.next
