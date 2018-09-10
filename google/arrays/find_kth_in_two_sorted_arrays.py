class Solution:

    def findKth(self, nums1, nums2, k):
        if len(nums1) == 0:
            return nums2[k]
        if len(nums2) == 0:
            return nums1[k]

        mid1 = len(nums1)/2
        mid2 = len(nums2)/2

        if k > mid1 + mid2:
            if nums1[mid1] > nums2[mid2]:
                return self.findKth(nums1, nums2[mid2 + 1:], k - mid2 - 1)
            else:
                return self.findKth(nums1[mid1 + 1:], nums2, k - mid1 - 1)
        else:
            if nums1[mid1] > nums2[mid2]:
                return self.findKth(nums1[:mid1], nums2, k)
            else:
                return self.findKth(nums1, nums2[:mid2], k)

    def findMedianSortedArrays(self, nums1, nums2):
        total_length = len(nums1) + len(nums2)

        if total_length % 2 == 1:
            # odd case
            return self.findKth(nums1, nums2, total_length / 2)
        else:
            return (self.findKth(nums1, nums2, total_length / 2) + self.findKth(nums1, nums2, total_length/2 - 1))/2.

solution = Solution()

print solution.findMedianSortedArrays([1,3], [2])