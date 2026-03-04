from typing import Optional, List

# 23 合并k个排序链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for list in lists:
            while list:
                arr.append(list)
                list = list.next
        arr.sort(key=lambda x: x.val)
        dummy = ListNode(0)
        cur = dummy
        for node in arr:
            cur.next = node
            cur = cur.next
        return dummy.next