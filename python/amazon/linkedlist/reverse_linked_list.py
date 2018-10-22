# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        stack = []

        tmp = head
        while tmp:
            stack.append(tmp)
            tmp = tmp.next

        dummy = ListNode(None)
        tmp = dummy
        while len(stack) > 0:
            tmp.next = stack.pop()
            tmp = tmp.next
        tmp.next = None
        return dummy.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
result = solution.reverseList(node1)
i = 0
