from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p0 = dummy = ListNode(0,head)
        cur = dummy.next
        n = 0
        while cur:
            n += 1
            cur = cur.next
        pre,cur = None,dummy.next
        while n >= k:
            n -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            nxt = p0.next
            nxt.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next

if __name__ == "__main__":
    s = Solution()
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    print(s.reverseKGroup(head,2))

