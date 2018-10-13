# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        dummy = ListNode(None)
        current = dummy
        pq = PriorityQueue()
        for list in lists:
            if list:
                pq.put((list.val, list))

        while pq.qsize() > 0:
            current.next = pq.get()[1]
            current = current.next
            if current.next:
                pq.put((current.next.val, current.next))

        return dummy.next
