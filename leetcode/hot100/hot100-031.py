from typing import Optional

# 25 K 个一组翻转链表 这道题麻烦
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur: # 统计链表长度
            n += 1
            cur = cur.next
        p0 = dummy = ListNode(0, head)
        pre = None
        cur = head
        while n >= k:
            n -= k
            for _ in range(k):
                nex = cur.next
                cur.next = pre
                pre = cur
                cur = nex
            nex = p0.next
            nex.next = cur
            p0.next = pre
            p0 = nex
        return dummy.next


"""
翻转
"""