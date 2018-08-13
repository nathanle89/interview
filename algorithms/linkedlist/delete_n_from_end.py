# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        total_length = 0
        temp = head
        while temp:
            temp = temp.next
            total_length += 1

        index_node_before = total_length - n - 1

        if index_node_before < 0:
            temp = head.next
            head.next = None
            head = temp
        else:
            counter = 0
            current = head
            while counter < index_node_before:
                current = current.next
                counter += 1

            if current.next:
                current.next = current.next.next

        return head

node1 = ListNode(1)
node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)

node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

solution = Solution()
print(solution.removeNthFromEnd(node1, 2).val)

# print(node2)
# print(node1.val)
# print(node1.next.val)
# print(node1.next.next.val)
# print(node1.next.next.next.val)
