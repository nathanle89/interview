class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []

        sorted_list = []
        for list_node in lists:
            if list_node:
                heapq.heappush(sorted_list, (list_node.val, list_node))

        if len(sorted_list) == 0:
            return []

        dummy = ListNode(0)
        tmp = dummy
        while len(sorted_list) > 0:
            priority, next_node = heapq.heappop(sorted_list)
            tmp.next = next_node
            tmp = tmp.next

            if next_node.next:
                heapq.heappush(sorted_list, (next_node.next.val, next_node.next))

        return dummy.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)

node1.next = node2
node2.next = node3

node4 = ListNode(1)
node5 = ListNode(1)
node6 = ListNode(2)

node4.next = node5
node5.next = node6
#
# node7 = ListNode(2)
# node8 = ListNode(6)

# node7.next = node8
lists = [node1, node4]

solution = Solution()
result = solution.mergeKLists(lists)
i = 0
