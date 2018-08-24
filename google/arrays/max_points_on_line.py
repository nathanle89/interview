class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        length_points = len(points)
        if length_points == 1:
            return 1

        unique_points = {}
        for point in points:
            unique_points[(point.x, point.y)] = unique_points.get((point.x, point.y), 0) + 1

        result = 0
        P = unique_points.keys()

        if len(P) == 1:
            return unique_points.get(P[0])

        for i in range(0, len(P) - 1):
            slopes = {}
            current_max = 0
            for j in range(i+1, len(P)):
                point_i = P[i]
                point_j = P[j]

                dx, dy = point_i[0] - point_j[0], point_i[1] - point_j[1]

                if dx == 0:
                    slope = 'v'
                elif dy == 0:
                    slope = 'h'
                else:
                    slope = str(float(dy)/dx)

                slopes[slope] = slopes.get(slope, 0) + unique_points[(point_j[0], point_j[1])]
                current_max = max([current_max, slopes[slope]])
            result = max([result, unique_points[(point_i[0], point_i[1])] + current_max])

        return result
