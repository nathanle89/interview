class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        row_left_index = 0
        col_left_index = 0

        row_bottom_index = len(matrix) - 1
        col_bottom_index = len(matrix[0]) - 1
        results = []
        while row_left_index <= row_bottom_index and col_left_index <= col_bottom_index:
            # Top row
            for i in range(col_left_index, col_bottom_index):
                results.append(matrix[row_left_index][i])

            # Right col
            for i in range(row_left_index, row_bottom_index):
                results.append(matrix[i][col_bottom_index])

            if row_left_index < row_bottom_index:
                #botom row
                for i in reversed(range(col_left_index + 1, col_bottom_index + 1)):
                    results.append(matrix[row_bottom_index][i])
            elif col_left_index < col_bottom_index:
                results.append(matrix[row_left_index][col_bottom_index])

            if col_left_index < col_bottom_index:
                # Left col
                for i in reversed(range(row_left_index + 1, row_bottom_index + 1)):
                    results.append(matrix[i][col_left_index])
            elif row_left_index < row_bottom_index:
                results.append(matrix[row_bottom_index][col_left_index])

            if row_left_index == row_bottom_index and col_left_index == col_bottom_index:
                results.append(matrix[row_left_index][col_left_index])

            row_left_index += 1
            col_left_index += 1
            row_bottom_index -= 1
            col_bottom_index -= 1

        return results

matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution = Solution()

print solution.spiralOrder(matrix)