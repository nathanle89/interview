import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = {}
        self.list_items = []


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dictionary:
            return False
        else:
            self.list_items.append(val)
            self.dictionary[val] = len(self.list_items) - 1
            return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dictionary:
            return False

        # Basically we use the last item in the list as placeholder to remove
        # Grab the current index in the dict, and swap current index with the last element in the list
        # Update the current_index with the new element, kick the old val from the dict and pop the last item in the list

        current_index = self.dictionary[val]
        last = self.list_items[-1]
        self.list_items[current_index] = last
        self.dictionary[last] = current_index
        del self.dictionary[val]
        self.list_items.pop()

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.sample(self.list_items, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
