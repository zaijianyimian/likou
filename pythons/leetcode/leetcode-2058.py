# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        tmp = []
        dummy = ListNode(0, head)
        pre = dummy
        p = head
        ind = 0
        while p and p.next:
            if pre == dummy:
                pre = p
                p = p.next
                ind += 1
                continue
            if (p.val > pre.val and p.val > p.next.val) or (p.val < pre.val and p.val < p.next.val):
                tmp.append(ind)
            pre = p
            p = p.next
            ind += 1
        if len(tmp) < 2:
            return[-1,-1]
        maxInd = tmp[-1] - tmp[0]
        minInd = ind
        for i in range(1,len(tmp)):
            minInd = min(minInd, tmp[i] - tmp[i-1])
        return [minInd,maxInd]

