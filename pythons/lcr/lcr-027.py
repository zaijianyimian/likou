# Definition for singly-linked list.
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        que = collections.deque()
        p = head
        while p:
            que.append(p.val)
            p = p.next
        while que:
            if len(que) == 1:
                return True
            leftNode = que.popleft()
            rightNode = que.pop()
            if leftNode != rightNode:
                return False
        return True
