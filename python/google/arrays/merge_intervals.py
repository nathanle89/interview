"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        sorted_intervals = sorted(intervals, key=lambda x: x.start)

        merged = []
        for interval in sorted_intervals:
            if len(merged) == 0:
                merged.append([interval.start, interval.end])
            else:
                # Check for overlapp
                if interval.start <= merged[-1][-1]:
                    merged[-1] = [min(merged[-1][0], interval.start), max(merged[-1][-1], interval.end)]
                else:
                    merged.append([interval.start, interval.end])

        return merged

solution = Solution()
interval1 = Interval(1,3)
interval2 = Interval(2,6)
interval3 = Interval(8,10)
interval4 = Interval(15,18)

print solution.merge([interval1, interval2, interval3, interval4])
print solution.merge([Interval(1,4), Interval(4,5)])