class DoubleLinkedNode(object):

    def __init__(self, val):
        self.val = val
        self.previous = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        # Read key and update least recently use sequence
        value, reference = self.cache[key]

        self.updateRecency(key)             
        
        return value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            current_value, reference = self.cache[key]
            self.updateRecency(key)
            self.cache[key] = (value, reference)
            return

        current_size = len(self.cache)
        if current_size == self.capacity:
            # kick stuff out
            del self.cache[self.head.val]
            current_head = self.head
            self.head = current_head.next
            current_head.next = None # Dereference
            if self.head:
                self.head.previous = None

        # Add the new Node
        reference = DoubleLinkedNode(key)

        if self.tail:
            self.tail.next = reference
            reference.previous = self.tail
            self.tail = reference

        if not self.head:
            self.head = reference
        if not self.tail:
            self.tail = reference

        self.cache[key] = (value, reference)
            
        
    def updateRecency(self, key):
        # Read key and update least recently use sequence
        value, reference = self.cache[key]
        
        # Move reference to the tail
        previous_reference = reference.previous
        next_reference = reference.next

        current_tail = self.tail

        # Reconnect current missing link
        if previous_reference and next_reference:
            # Reference is in the middle
            previous_reference.next = next_reference
            next_reference.previous = previous_reference
        elif next_reference:
            # reference is the first node
            next_reference.previous = None
            self.head = next_reference

        # Move it to the end
        if reference != current_tail:
            reference.previous = current_tail
            current_tail.next = reference
        reference.next = None
        self.tail = reference

# Your LRUCache object will be instantiated and called as such:
# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# print cache.get(1)
# cache.put(3, 3)
# print cache.get(2)
# cache.put(4, 4)
# print cache.get(1)
# print cache.get(3)
# print cache.get(4)

# ["LRUCache","put","get","put","get","get"]
# [[1],[2,1],[2],[3,2],[2],[3]]

# cache = LRUCache(1)
# cache.put(2, 1)
# print cache.get(2)
# cache.put(3, 2)
# print cache.get(2)
# print cache.get(3)


# ["LRUCache","put","put","get","put","put","get"]
# [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]

cache = LRUCache(2)
cache.put(2, 1)
cache.put(2, 2)
print cache.get(2)
cache.put(1, 1)
cache.put(4, 1)
print cache.get(2)
