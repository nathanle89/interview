import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = list(nums)
        self.current = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.current = list(self.original)
        return self.current

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(0, len(self.current)):
            random_index = random.randint(0, len(self.current) - 1)
            temp = self.current[i]
            self.current[i] = self.current[random_index]
            self.current[random_index] = temp

        return self.current
nums = [1,2,3]
solution = Solution(nums)

print(solution.shuffle())