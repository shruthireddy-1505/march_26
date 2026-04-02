# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddDummy = ListNode(-1)
        evenDummy = ListNode(-1)
        oddTail = oddDummy
        evenTail = evenDummy
        count = 1
        curr = head
        while curr:
            if count%2 != 0:
                oddTail.next = curr
                oddTail = oddTail.next
            else:
                evenTail.next = curr
                evenTail = evenTail.next 
            curr = curr.next
            count += 1
        evenTail.next = None
        oddTail.next = evenDummy.next
        return oddDummy.next



        