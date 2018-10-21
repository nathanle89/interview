# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if not head:
            return None

        cloned_map = {}

        cloned_head = RandomListNode(head.label)
        tmp_head = head
        tmp_cloned_head = cloned_head
        cloned_map[head] = cloned_head

        while tmp_head.next:
            next_head = tmp_head.next

            cloned_next_head = RandomListNode(next_head.label)
            tmp_cloned_head.next = cloned_next_head
            cloned_map[next_head] = cloned_next_head

            tmp_cloned_head = tmp_cloned_head.next
            tmp_head = tmp_head.next


        tmp_head = head
        tmp_cloned_head = cloned_head

        while tmp_head:
            if tmp_head.random:
                tmp_cloned_head.random = cloned_map[tmp_head.random]

            tmp_head = tmp_head.next
            tmp_cloned_head = tmp_cloned_head.next


        return cloned_head
