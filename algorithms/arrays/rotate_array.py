class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for index in range(0, k):
            val = nums.pop()
            nums.insert(0, val)

nums = [1, 2, 3, 4, 5, 6, 7]
solution = Solution()
solution.rotate(nums, 5)
print(nums)
