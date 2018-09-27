class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        previous_index = 0
        total_profit = 0
        for index in range(0, len(prices)):
            if previous_index == index:
                continue

            previous_price = prices[previous_index]
            current_price = prices[index]

            if previous_price < current_price:
                total_profit += current_price - previous_price

            previous_index += 1

        return total_profit

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_nums = len(nums)

        if length_nums == 0:
            return 0

        previous_index = 0
        current_index = 1

        while current_index < length_nums:
            previous_num = nums[previous_index]
            current_num = nums[current_index]

            if previous_num == current_num:
                del nums[current_index]
                length_nums -= 1
            else:
                previous_index = current_index
                current_index += 1

        return current_index

solution = Solution()

# print(solution.maxProfit([7,1,5,3,6,4]))
# print(solution.maxProfit([1,2,3,4,5]))
# print(solution.maxProfit([7,6,4,3,1]))
#

nums = [0,0,1,1,1]
print(solution.removeDuplicates(nums))
print(nums)
