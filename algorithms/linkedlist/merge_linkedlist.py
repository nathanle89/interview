# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # Edge cases
        if l1 is None and l2 is None:
            return
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        # Capture return value
        if l1.val <= l2.val:
            head = l1
        else:
            head = l2

        # Core logic
        next_l1 = l1
        next_l2 = l2
        current = None
        while next_l1 and next_l2:
            if next_l1.val <= next_l2.val:
                temp = next_l1.next
                if current is None:
                    current = next_l1
                else:
                    current.next = next_l1
                    current = current.next
                next_l1 = temp
            else:
                temp = next_l2.next
                if current is None:
                    current = next_l2
                else:
                    current.next = next_l2
                    current = current.next
                next_l2 = temp

        if next_l1 is not None:
            current.next = next_l1
        elif next_l2 is not None:
            current.next = next_l2

        return head

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node4 = ListNode(1)
node5 = ListNode(9)
node6 = ListNode(15)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

solution = Solution()
head = solution.mergeTwoLists(node1, node4)
i = 0
