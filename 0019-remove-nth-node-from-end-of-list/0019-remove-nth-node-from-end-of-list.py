# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        l = 0
        while temp:
            l+=1
            temp = temp.next
        c = abs(n-l)
        curr = head
        if c == 0:
            return head.next
        t = 0
        while curr:
            t += 1
            if t == c:
                curr.next = curr.next.next
            curr = curr.next
        return head

