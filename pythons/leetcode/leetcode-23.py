from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for i in lists:
            while i:
                arr.append(i)
                i = i.next
        arr.sort(key = lambda x: x.val)
        dummy = ListNode()
        cur = dummy
        for node in arr:
            cur.next = node
            cur = cur.next
        return dummy.next

