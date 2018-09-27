class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        self.rotateHelper(0, 0, len(matrix) - 1, len(matrix[0]) - 1, matrix)

    def rotateHelper(self, top_left_y_index, top_left_x_index, bottom_right_y_index, bottom_right_x_index, matrix):
        if top_left_y_index >= bottom_right_y_index or top_left_x_index >= bottom_right_x_index:
            return

        horizontal_length = bottom_right_x_index - top_left_x_index
        vertical_length = bottom_right_y_index - top_left_y_index

        for index in range(0, horizontal_length):
            top_left_val = matrix[top_left_y_index][top_left_x_index + index]

            top_right_val = matrix[top_left_y_index + index][top_left_x_index + horizontal_length]

            bottom_right_val = matrix[bottom_right_y_index][bottom_right_x_index - index]

            bottom_left_val = matrix[top_left_y_index + vertical_length - index][top_left_x_index]

            matrix[top_left_y_index][top_left_x_index + index] = bottom_left_val
            matrix[top_left_y_index + index][top_left_x_index + horizontal_length] = top_left_val
            matrix[bottom_right_y_index][bottom_right_x_index - index] = top_right_val
            matrix[top_left_y_index + vertical_length - index][top_left_x_index] = bottom_right_val

        self.rotateHelper(top_left_y_index + 1, top_left_x_index + 1, bottom_right_y_index - 1, bottom_right_x_index - 1, matrix)


solution = Solution()

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
solution.rotate(matrix)
print(matrix)

matrix = [
    [ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]
]

solution.rotate(matrix)
print(matrix)
