# Definition for singly-linked list.
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        que = collections.deque()
        p = head
        dummy = ListNode()
        while p:
            que.append(p)
            p = p.next
        flag = 0
        p = dummy
        while que:
            if flag == 0:
                node = que.popleft()
                flag = 1
            else:
                node = que.pop()
                flag = 0
            p.next = node
            p = p.next
        p.next = None
