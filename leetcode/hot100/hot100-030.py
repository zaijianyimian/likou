from typing import Optional

# 24. 两两交换链表中的节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next: # 这里为什么不能只判断cur.next.next? 防止出现空指针问题
            node1 = cur.next
            node2 = cur.next.next
            node1.next = node2.next
            node2.next = node1
            cur.next = node2
            cur = node1
        return dummy.next
