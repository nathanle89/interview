class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        seen_number = {}
        seen_results = {}

        for num in nums:
            if num in seen_number:
                seen_number[num] = 1 + seen_number[num]
            else:
                seen_number[num] = 1

        results = []

        for num in nums:
            matching_sum_val = target - num

            if matching_sum_val in seen_number:
                if num == matching_sum_val and not seen_number[matching_sum_val] > 1:
                    continue

                if matching_sum_val < num:
                    result = [matching_sum_val, num]
                    result_string = str(matching_sum_val) + str(num)
                else:
                    result = [num, matching_sum_val]
                    result_string = str(num) + str(matching_sum_val)

                if result_string not in seen_results:
                    results.append(result)
                    seen_results[result_string] = True

        return results

solution = Solution()

print solution.twoSum([-1, 0, 1, 2, -1, -4, -2, -3], -5)
