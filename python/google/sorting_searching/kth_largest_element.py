import heapq

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        heap = []
        for i in range(0, len(nums)):
            heapq.heappush(heap, nums[i])
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)

nums = [3,2,1,5,6,4]
k = 2

solution = Solution()
print solution.findKthLargest(nums, k)