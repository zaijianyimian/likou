from platform import node
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0, head)
        cur = head
        num = []
        while cur:
            num.append(cur)
            cur = cur.next
        num1 = num[:len(num)//2]
        num2 = num[len(num)//2:]
        num2.reverse()
        for i in range(len(num1)):
            num1[i].next = num2[i]
            if i != len(num1) - 1:
                num2[i].next = num1[i+1]
            else:
                num2[i].next = None
        if len(num1) != len(num2):
            num2[-2].next = num2[-1]
        num2[-1].next = None
        return dummy.next

