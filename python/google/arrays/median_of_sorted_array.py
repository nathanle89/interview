class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        length_nums1 = len(nums1)
        length_nums2 = len(nums2)

        total_length = length_nums1 + length_nums2
        is_even = False
        if total_length % 2 == 0:
            is_even = True

        median_index = total_length / 2 # round down

        nums1_index = 0
        nums2_index = 0
        current_counter = -1
        current_val = -1
        previous_val = -1

        while nums1_index < length_nums1 and nums2_index < length_nums2:
            if nums1[nums1_index] <= nums2[nums2_index]:
                previous_val = current_val
                current_val = nums1[nums1_index]
                nums1_index += 1
            else:
                previous_val = current_val
                current_val = nums2[nums2_index]
                nums2_index += 1
            current_counter += 1

            if current_counter == median_index:
                return self.computeResult(current_val, previous_val, is_even)

        if current_counter < median_index:
            if nums1_index == length_nums1:
                while nums2_index < length_nums2:
                    previous_val = current_val
                    current_val = nums2[nums2_index]
                    nums2_index += 1
                    current_counter += 1
                    if current_counter == median_index:
                        return self.computeResult(current_val, previous_val, is_even)

            else:
                while nums1_index < length_nums1:
                    previous_val = current_val
                    current_val = nums1[nums1_index]
                    nums1_index += 1
                    current_counter += 1
                    if current_counter == median_index:
                        return self.computeResult(current_val, previous_val, is_even)
                # nums1 has more to go

    def computeResult(self, current_val, previous_val, is_even):
        if is_even:
            return (current_val + previous_val)/2.
        else:
            return float(current_val)


solution = Solution()

nums1 = [1, 3]
nums2 = [2]

nums3 = [1, 2]
nums4 = [3, 4]

nums7 = [3]
nums8 = [1,2,4, 5, 6]

nums5 = []
nums6 = [1]

print(solution.findMedianSortedArrays(nums1, nums2))
