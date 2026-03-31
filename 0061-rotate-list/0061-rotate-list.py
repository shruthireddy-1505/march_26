# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        dup = head
        l = 1
        c = 0
        while dup.next:
            l += 1

            dup = dup.next
        if k%l == 0:
            return head
        n = k%l
        
        rm = l - n
        curr = head

        dup.next = head
        while curr:
            c += 1
            if c==rm:
                head = curr.next
                curr.next = None
                break

            curr = curr.next

        return head
        