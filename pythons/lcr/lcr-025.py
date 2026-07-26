# Definition for singly-linked list.
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        queue1 = collections.deque()
        queue2 = collections.deque()
        p = l1
        while p:
            queue1.append(p.val)
            p = p.next
        p = l2
        while p:
            queue2.append(p.val)
            p = p.next
        carry = 0
        dummy = ListNode()
        while queue1 or queue2 or carry:
            num1 = queue1.pop() if queue1 else 0
            num2 = queue2.pop() if queue2 else 0

            total = num1 + num2 + carry

            carry = total // 10  # 进位
            node = ListNode(total % 10)  # 当前位

            node.next = dummy.next
            dummy.next = node

        return dummy.next
