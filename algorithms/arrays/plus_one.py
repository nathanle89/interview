class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return self.plusOneHelper(digits)

    def plusOneHelper(self, digits):
        result = list(digits)
        last_number = result[-1]

        if last_number < 9:
            last_number += 1
            result[-1] = last_number
        else:
            digits_length_minus_one = len(result) - 1

            if digits_length_minus_one == 0:
                result = [1, 0]
            else:
                updated = self.plusOneHelper(digits[0:-1])
                updated.append(0)
                result = updated

        return result

solution = Solution()

print(solution.plusOne([1,9,9,9]))
