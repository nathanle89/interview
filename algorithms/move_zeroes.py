class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        current_index = 0
        length = len(nums)

        for index in range(0, length):
            if nums[index] != 0:
                nums[current_index] = nums[index]
                current_index += 1

        while current_index < length:
            nums[current_index] = 0
            current_index += 1
