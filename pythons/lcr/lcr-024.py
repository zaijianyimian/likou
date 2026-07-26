# Definition for singly-linked list.
from multiprocessing import dummy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummy = ListNode(next=None)
        p = head
        while p:
            tmp = p.next
            p.next = dummy.next
            dummy.next = p
            p = tmp
        return dummy.next
