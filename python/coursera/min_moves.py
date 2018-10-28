class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min(nums)
        moves = 0

        for i in range(len(nums)):
            moves += nums[i] - min_num

        return moves
