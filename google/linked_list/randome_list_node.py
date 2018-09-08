"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""
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
        if head is None:
            return None

        newHead = RandomListNode(head.label)
        cloneMap = dict()
        cloneMap[head] = newHead

        currentOriginal = head
        currentClone = newHead
        while currentOriginal.next is not None:
            currentOriginal = currentOriginal.next

            newNode = RandomListNode(currentOriginal.label)
            currentClone.next = newNode
            cloneMap[currentOriginal] = newNode

            currentClone = currentClone.next

        currentOriginal = head
        currentClone = newHead

        while currentOriginal is not None:
            if currentOriginal.random is not None:
                currentClone.random = cloneMap[currentOriginal.random]

            currentOriginal = currentOriginal.next
            currentClone = currentClone.next

        return newHead