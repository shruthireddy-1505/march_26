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
        """
        time optimiztion

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
        """

        ltempA = headA
        tempA = headA

        ltempB = headB
        tempB = headB

        count1 = 0
        count2 = 0
        while ltempA:
            count1+=1
            ltempA = ltempA.next
        while ltempB:
            count2+=1
            ltempB = ltempB.next
        while count1>count2:
            tempA = tempA.next
            count1 -= 1
        while count2>count1:
            tempB = tempB.next
            count2 -= 1
        while tempA!=tempB:
            tempA = tempA.next
            tempB = tempB.next
        return tempA



        