"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        # Find the heighest point
        heighest_pillar = max(height)
        index_heighest_pillar = height.index(heighest_pillar)

        left_side = height[0:index_heighest_pillar+1] # including the heighest pillar
        right_side = height[index_heighest_pillar:]
        right_side.reverse()

        return self.calculate_water(left_side) + self.calculate_water(right_side)

    def calculate_water(self, height):
        found_start_pillar = False
        water_amount = 0
        current_pillar = 0
        for pillar in height:
            if pillar > 0 and found_start_pillar:
                found_start_pillar = True
                current_pillar = pillar
            else:
                # Now we found the entree point
                if pillar < current_pillar:
                    # This means we have a valley
                    water_amount += current_pillar - pillar
                else:
                    # We found a new higher pillar
                    current_pillar = pillar
        return water_amount

solution = Solution()

print solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])