# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast = head
        slow = head

        while slow and fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next

            if fast and slow and fast == slow:
                return True

        return False

