class Solution:
    def productExceptSelf(self, nums):
        if len(nums) == 0:
            return []

        # first pass
        temp_array = [1] * len(nums)
        current_product = 1
        for i in range(len(nums)):
            current_product *= nums[i]
            if i < len(nums) - 1:
                temp_array[i + 1] = current_product

        current_product = 1
        for i in reversed(range(len(nums))):
            current_product *= nums[i]
            if i > 0:
                temp_array[i - 1] = current_product * temp_array[i - 1]

        return temp_array

solution = Solution()
print(solution.productExceptSelf([2,3,4,5]))