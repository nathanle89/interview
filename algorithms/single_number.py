class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dup_num_dict = {}
        single_num_dict = {}

        for num in nums:
            if num in single_num_dict:
                single_num_dict.pop(num, None)
                dup_num_dict[num] = True
            else:
                single_num_dict[num] = True

        results = list(single_num_dict.keys())

        if len(results) > 0:
            return results[0]
        else:
            return None

solution = Solution()

print(solution.singleNumber([4,1,2,1,2]))
