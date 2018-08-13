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
            return

        temp = head
        stack = []
        while temp:
            stack.append(temp)
            temp = temp.next

        tail = stack.pop()
        head = tail
        while len(stack) > 0:
            next_tail = stack.pop()
            tail.next = next_tail
            tail = next_tail

        tail.next = None

        return head

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

solution = Solution()
print(solution.reverseList(node1))
