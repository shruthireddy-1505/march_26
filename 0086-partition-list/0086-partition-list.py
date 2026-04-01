# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        sDummy = ListNode(-1)
        gDummy = ListNode(-1)
        sTail = sDummy
        gTail = gDummy
        curr = head
        while curr:
            if curr.val<x:
                sTail.next = curr
                sTail = sTail.next
            else:
                gTail.next = curr
                gTail = gTail.next
            curr = curr.next
        gTail.next = None
        sTail.next = gDummy.next
        return sDummy.next
        