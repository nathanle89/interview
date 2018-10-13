# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        tmp1 = l1
        tmp2 = l2
        head = None
        result = None
        remainder = 0
        while tmp1 and tmp2:
            sum = tmp1.val + tmp2.val + remainder
            if sum >= 10:
                remainder = 1
                sum -= 10
            else:
                remainder = 0

            if head is None:
                head = ListNode(sum)
                result = head
            else:
                head.next = ListNode(sum)
                head = head.next

            tmp1 = tmp1.next
            tmp2 = tmp2.next

        if tmp1 is not None:
            if remainder > 0:
                while tmp1:
                    sum = tmp1.val + remainder
                    if sum >= 10:
                        remainder = 1
                        sum -= 10
                    else:
                        remainder = 0

                    head.next = ListNode(sum)
                    head = head.next
                    tmp1 = tmp1.next
                if remainder > 0:
                    head.next = ListNode(remainder)
            else:
                head.next = tmp1
        elif tmp2 is not None:
            if remainder > 0:
                while tmp2:
                    sum = tmp2.val + remainder
                    if sum >= 10:
                        remainder = 1
                        sum -= 10
                    else:
                        remainder = 0

                    head.next = ListNode(sum)
                    head = head.next
                    tmp2 = tmp2.next
                if remainder > 0:
                    head.next = ListNode(remainder)
            else:
                head.next = tmp2
        else:
            if remainder > 0:
                head.next = ListNode(remainder)

        return result