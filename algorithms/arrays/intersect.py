class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ref = {}
        for num in nums1:
            ref[num] = ref.get(num, 0) + 1

        inter = []

        for num in nums2:
            if num in ref and ref[num] > 0:
                inter.append(num)
                ref[num] -= 1

        return inter

solution = Solution()

print(solution.intersect([1, 2, 2, 1], [2, 2]))
