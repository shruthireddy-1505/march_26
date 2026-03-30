# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        point = dummy
        while point.next and point.next.next:
            s1 = point.next
            s2 = point.next.next
            
            s1.next = s2.next
            s2.next = s1

            point.next = s2
            point = s1
        return dummy.next
        