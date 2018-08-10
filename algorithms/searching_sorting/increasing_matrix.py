class Solution:
    def findElement(self, matrix, element):
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if matrix[row][col] == element:
                return True
            elif matrix[row][col] > element:
                col -= 1
            else:
                row += 1

        return False

matrix = [
    [15, 20, 40, 85],
    [20, 35, 80, 95],
    [30, 55, 95, 105],
    [40, 80, 100, 120]
]

solution = Solution()
print(solution.findElement(matrix, 106))