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
        current_length = len(self.current)
        copied_original = list(self.original)
        randomized_list = []
        while len(copied_original) > 0:
            random_generate_index = random.randint(0, current_length - 1)
            randomized_list.append(copied_original[random_generate_index])
            del copied_original[random_generate_index]
            current_length -= 1

        return randomized_list

nums = [1,2,3]
solution = Solution(nums)

print(solution.shuffle())