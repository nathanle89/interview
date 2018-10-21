class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        # Find the highest pillar
        max_pillar = max(height)
        index_max_pillar = height.index(max_pillar)

        left_pillars = height[:index_max_pillar+1] # Including index_max_pillar
        right_pillars = height[index_max_pillar:]
        right_pillars.reverse()

        return self.calculateRain(left_pillars) + self.calculateRain(right_pillars)

    def calculateRain(self, pillars):
        start_index = -1
        total_rain = 0

        for i in range(len(pillars)):
            # Look for the first pillar
            if start_index < 0:
                if pillars[i] > 0:
                    start_index = i
            else:
                # Found the first pillar
                if pillars[i] < pillars[start_index]:
                    total_rain += pillars[start_index] - pillars[i]
                else:
                    start_index = i

        return total_rain

heights = [0,1,0,2,1,0,1,3,2,1,2,1]
solution = Solution()

print solution.trap(heights)
