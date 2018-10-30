class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) == 0:
            return self.medianOfArray(nums2)

        if len(nums2) == 0:
            return self.medianOfArray(nums1)

        if len(nums1) <= len(nums2):
            smaller_array = nums1
            larger_array = nums2
        else:
            smaller_array = nums2
            larger_array = nums1
        total_length = len(smaller_array) + len(larger_array)
        total_even = False
        if total_length % 2 == 0:
            total_even = True

        start = 0
        end = len(smaller_array)

        while start <= end:
            partition_X = (start + end)/2
            partition_Y = (len(smaller_array) + len(larger_array) + 1)/2 - partition_X

            max_left_x = None
            max_left_y = None
            min_right_x = None
            min_right_y = None

            if partition_X == 0:
                max_left_x = -2**31 # -Infinity
            if partition_Y == 0:
                max_left_y = -2**31 # -Infinity
            if partition_X == len(smaller_array):
                min_right_x = 2**31 # Infinity
            if partition_Y == len(larger_array):
                min_right_y = 2**31 # Infinity

            if max_left_x is None:
                max_left_x = smaller_array[partition_X - 1]
            if max_left_y is None:
                max_left_y = larger_array[partition_Y - 1]
            if min_right_x is None:
                min_right_x = smaller_array[partition_X]
            if min_right_y is None:
                min_right_y = larger_array[partition_Y]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if total_even:
                    return sum([max(max_left_x, max_left_y), min(min_right_x, min_right_y)])/2.0
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y:
                end = partition_X - 1
            else:
                start = partition_X + 1

    def medianOfArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return (nums[0] + nums[1])/2.0

        mid = len(nums)/2
        if len(nums) % 2 == 0:
            return (nums[mid] + nums[mid - 1])/2.0
        else:
            return nums[mid]