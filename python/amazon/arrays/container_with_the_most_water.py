class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        max_water = -1

        while start < end:
            # Calculate area
            container_height = min(height[start], height[end])
            container_width = end - start

            area = container_width * container_height
            if area > max_water:
                max_water = area

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_water
