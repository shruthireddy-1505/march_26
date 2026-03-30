# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """ 
        time limit exceed
        tempA = headA
        tempB = headB
        while tempA:
            dum = tempB
            while dum:
                if tempA == dum:
                    return tempA
                dum = dum.next
            tempA = tempA.next
        return None
        """
        s = set()
        tempA = headA
        while tempA:
            s.add(tempA)
            tempA = tempA.next
        tempB = headB
        while tempB:
            if tempB in s:
                return tempB
            tempB = tempB.next
        return None

        