# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        # Edge cases
        if head is None:
            return True

        stack = []
        temp = head
        length_counter = 0
        while temp:
            stack.append(temp)
            temp = temp.next
            length_counter += 1

        temp = head
        counter = 0
        while counter < (length_counter / 2) + 1:
            tail_val = stack.pop()

            if tail_val.val != temp.val:
                return False

            # Forward temp
            temp = temp.next

            counter += 1

        return True
