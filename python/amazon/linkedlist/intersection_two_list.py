# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        tmpA = headA
        tmpB = headB

        while tmpA is not tmpB:

            if tmpA is None:
                tmpA = headB
            else:
                tmpA = tmpA.next

            if tmpB is None:
                tmpB = headA
            else:
                tmpB = tmpB.next

        # Once we switch head, both list will catch up with the difference in length and will end up at the same position
        # Or None on both
        # We run at max 2 run on each list so O(N) and no extra space needed O(1)
        return tmpA