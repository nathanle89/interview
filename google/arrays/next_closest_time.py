"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
"""

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        # Generate possible times
        possible_nums = set()
        for char in time:
            if char != ':':
                possible_nums.add(char)

        if len(possible_nums) == 1:
            return time

        all_possible_time = []
        for num1 in possible_nums:
            for num2 in possible_nums:
                for num3 in possible_nums:
                    for num4 in possible_nums:
                        possible_time = num1 + num2 + ':' + num3 + num4
                        if self.isValidTime(possible_time) and possible_time != time:
                            all_possible_time.append(possible_time)
        min_diff = 2**32
        result = None
        for each_time in all_possible_time:
            diff = self.timeDiffMinutes(each_time, time)
            if min_diff > diff:
                min_diff = diff
                result = each_time

        return result

    def timeDiffMinutes(self, time1, time2):
        hour_diff = (int(time1[0:2]) - int(time2[0:2])) * 60
        min_diff = int(time1[3:]) - int(time2[3:])

        total_min_diff = hour_diff + min_diff

        if total_min_diff < 0:
            return total_min_diff + 24*60
        else:
            return total_min_diff


    def isValidTime(self, time):
        if len(time) != 5:
            return False

        if int(time[0:2]) <= 23 and int(time[3:]) <= 59:
            return True

solution = Solution()

print solution.nextClosestTime("00:00")