class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length_height = len(height)
        start_index = 0
        end_index = length_height - 1
        max_water = 0
        while start_index < end_index:
            current = height[start_index]
            end = height[end_index]

            area = min([current, end]) * (end_index - start_index)
            if area > max_water:
                max_water = area

            if current >= end:
                end_index -= 1
            else:
                start_index += 1
        return max_water

solution = Solution()

print solution.maxArea([1,8,6,2,5,4,8,3,7])
