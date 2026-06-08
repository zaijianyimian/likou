# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        se = set()
        p = head
        while p:
            if p not in se:
                se.add(p)
            else:
                return p
            p = p.next
        return None
