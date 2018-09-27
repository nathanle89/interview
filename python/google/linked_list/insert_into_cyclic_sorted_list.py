
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if head is None:
            return Node(insertVal, None)

        tmp = head
        loop_counter = 0
        # Try to find the min and max node in the list
        minNode = head
        largestNode = head
        while tmp != head or loop_counter == 0:
            if minNode.val > tmp.val:
                minNode = tmp
            if largestNode.val <= tmp.val:
                largestNode = tmp

            tmp = tmp.next
            if tmp == head:
                loop_counter += 1

        # flatten the list
        largestNode.next = None

        # Find a place to insert the new node
        if insertVal <= minNode.val or insertVal >= largestNode.val:
            newNode = Node(insertVal, minNode)
            largestNode.next = newNode
        else:
            # The new node is in the middle
            tmp = minNode
            while tmp is not None:
                if tmp.val < insertVal and insertVal <= tmp.next.val:
                    newNode = Node(insertVal, tmp.next)
                    tmp.next = newNode
                    break
                tmp = tmp.next
            largestNode.next = minNode

        return head

node1 = Node(3, None)
node2 = Node(3, None)
node3 = Node(3, None)

node1.next = node2
node2.next = node3
node3.next = node1

solution = Solution()

print solution.insert(node1, 2)