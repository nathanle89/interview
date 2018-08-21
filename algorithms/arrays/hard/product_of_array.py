class Solution:
    def productExceptSelf(self, nums):
        if not nums:
            return []

        product_left = 1
        product_right = 1
        length_nums = len(nums)
        # left to right
        results = [1] * length_nums

        for i in range(0, length_nums):
            results[i] = product_left
            product_left *= nums[i]

        # right to left
        for i in reversed(range(0, length_nums)):
            results[i] *= product_right
            product_right *= nums[i]

        return results

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))