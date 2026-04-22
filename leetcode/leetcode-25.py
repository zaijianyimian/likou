from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy.next
        n = 0
        while cur:
            n += 1
            cur = cur.next
        if n < k:
            return dummy.next
        pre = dummy
        start = dummy.next
        end = self.toend(dummy.next,k)
        while n >= k:
            nxt = end.next
            pre.next = self.reverse(start,end)
            start.next = nxt
            n -= k
            if n < k:
                break
            pre = start
            start = nxt
            end = self.toend(nxt,k)

        return dummy.next
    def toend(self,node,k):
        for i in range(k - 1):
            node = node.next
        return node
    def reverse(self,start,end) -> Optional[ListNode]:
        pre = None
        cur =  start
        ended = end.next
        while cur != end:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        cur.next = pre
        return end


