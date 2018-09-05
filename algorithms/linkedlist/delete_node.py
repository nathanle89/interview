# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next is None:
            return
        current_node = node

        while current_node.next.next is not None:
            current_node.val = current_node.next.val
            current_node = current_node.next

        current_node.val = current_node.next.val
        current_node.next = None


node1 = ListNode(4)
node2 = ListNode(5)
node3 = ListNode(1)
node4 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4

solution = Solution()
solution.deleteNode(node4)

print(node1.val)
print(node1.next.val)
print(node1.next.next.val)
print(node1.next.next.next.val)
