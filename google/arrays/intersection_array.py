"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

"""

class Solution:
    def intersection(self, nums1, nums2):

        # loop through nums1
        nums1_counter = {}
        for num in nums1:
            nums1_counter[num] = nums1_counter.get(num, 0) + 1

        results = []
        for num in nums2:
            if num in nums1_counter:
                del nums1_counter[num]
                results.append(num)

        return results
