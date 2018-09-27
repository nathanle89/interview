"""
Given a 2D integer matrix M representing the gray scale of an image,
you need to design a smoother to make the gray scale of each cell becomes the
average gray scale (rounding down) of all the 8 surrounding cells and itself.
If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].

"""

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if M is None:
            return []

        row_length = len(M)
        if row_length == 0:
            return []

        col_length = len(M[0])

        output = [[0] * col_length for i in range(row_length)]

        for i in range(0, row_length):
            for j in range(0, col_length):
                total_cell = 0
                sum = 0

                upper_left = self.get_value((i - 1, j - 1), M, row_length, col_length)
                upper = self.get_value((i - 1, j), M, row_length, col_length)
                upper_right = self.get_value((i - 1, j + 1), M, row_length, col_length)
                right = self.get_value((i, j + 1), M, row_length, col_length)
                bottom_right = self.get_value((i + 1, j + 1), M, row_length, col_length)
                bottom = self.get_value((i + 1, j), M, row_length, col_length)
                bottom_left = self.get_value((i + 1, j - 1), M, row_length, col_length)
                left = self.get_value((i, j - 1), M, row_length, col_length)

                if upper_left is not None:
                    total_cell += 1
                    sum += upper_left

                if upper is not None:
                    total_cell += 1
                    sum += upper

                if upper_right is not None:
                    total_cell += 1
                    sum += upper_right

                if right is not None:
                    total_cell += 1
                    sum += right

                if bottom_right is not None:
                    total_cell += 1
                    sum += bottom_right

                if bottom is not None:
                    total_cell += 1
                    sum += bottom

                if bottom_left is not None:
                    total_cell += 1
                    sum += bottom_left

                if left is not None:
                    total_cell += 1
                    sum += left

                total_cell += 1
                sum += M[i][j]

                output[i][j] = int(sum/total_cell)

        return output

    def get_value(self, index_tuple, M, row_length, col_length):
        if index_tuple[0] >= 0 and index_tuple[0] < row_length and index_tuple[1] >= 0 and index_tuple[1] < col_length:
            return M[index_tuple[0]][index_tuple[1]]
        else:
            return None

solution = Solution()
M = [[1,1,1],
     [1,0,1],
     [1,1,1]]
print(solution.imageSmoother(M))
