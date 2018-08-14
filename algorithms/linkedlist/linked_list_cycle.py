class Solution:
    def hasCycle(self, head):
        if head is None:
            return False

        slow = head
        fast = head

        while fast:
            slow = slow.next
            fast = fast.next

            if fast and fast.next:
                fast = fast.next

                # Check memory address
                if slow == fast:
                    return True

            else:
                return False

        return False
