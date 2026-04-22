from typing import Optional

# 148 排序链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        dummy = ListNode(0,head)
        while head:
            arr.append(head.val)
            head = head.next
        arr.sort()
        cur = dummy
        for i in arr:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next
