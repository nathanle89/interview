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
        # Handle base cases
        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        result = None
        carry_on = 0
        while l1 and l2:
            sum = l1.val + l2.val
            if carry_on:
                sum += carry_on
                carry_on = 0

            if sum > 9:
                if result is None:
                    result = ListNode(sum - 10)
                    head = result
                else:
                    result.next = ListNode(sum - 10)
                    result = result.next
                carry_on = 1
            else:
                if result is None:
                    result = ListNode(sum)
                    head = result
                else:
                    result.next = ListNode(sum)
                    result = result.next

            l1 = l1.next
            l2 = l2.next

        if l1 is not None:
            result.next = l1
            if carry_on > 0:
                while l1:
                    sum = l1.val + carry_on
                    if sum > 9:
                        l1.val = 0
                        carry_on = 1
                        l1 = l1.next
                    else:
                        l1.val = sum
                        carry_on = 0
                        break

        else:
            result.next = l2
            if carry_on > 0:
                while l2:
                    sum = l2.val + carry_on
                    if sum > 9:
                        l2.val = 0
                        carry_on = 1
                        l2 = l2.next
                    else:
                        l2.val = sum
                        carry_on = 0
                        break

        if carry_on > 0:
            temp = head
            while temp.next:
                temp = temp.next
            temp.next = ListNode(1)

        return head

node1 = ListNode(5)
# node2 = ListNode(4)
# node3 = ListNode(3)
# node1.next = node2
# node2.next = node3


node4 = ListNode(5)
# node5 = ListNode(6)
# node6 = ListNode(4)
#
# node4.next = node5
# node5.next = node6

solution = Solution()
print(solution.addTwoNumbers(node1, node4))
