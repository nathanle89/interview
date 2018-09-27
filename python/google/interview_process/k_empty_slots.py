"""
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

If there isn't such day, output -1.
"""

class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        number_flowers = len(flowers)
        if number_flowers < 2:
            return -1

        if k == 0:
            return 2

        if k > 0 and number_flowers < k + 2:
            return -1

        flowers_slot = [-1] * number_flowers

        for i in range(1, number_flowers + 1):
            flower_position = flowers[i - 1]
            flowers_slot[flower_position - 1] = flower_position
            flower_position_index = (flower_position - 1)
            # Checking for condition

            forward_position_flower_position_index = flower_position_index + k + 1
            backward_position_flower_position_index = flower_position_index - k - 1

            if forward_position_flower_position_index < number_flowers and flowers_slot[forward_position_flower_position_index] > -1:
                # Consider this block
                counter = 0
                if flowers_slot[flower_position_index + 1] == -1:
                    for j in range(flower_position_index+1, forward_position_flower_position_index):
                        if flowers_slot[j] == -1:
                            counter += 1
                    if counter == k:
                        return i

            if backward_position_flower_position_index >= 0 and flowers_slot[backward_position_flower_position_index] > -1:
                # Consider this block
                counter = 0
                if flowers_slot[flower_position_index - 1] == -1:
                    for j in range(backward_position_flower_position_index + 1, flower_position_index):
                        if flowers_slot[j] == -1:
                            counter += 1
                    if counter == k:
                        return i

        return -1


class BetterSolution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        garden = [[i-1, i+1] for i in range(len(flowers))]



solution = Solution()

print(solution.kEmptySlots([4,3,1,2], 1))
