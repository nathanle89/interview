"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1 -> 3 -> 1 -> 1 -> 1 minimizes the sum.
"""

class Solution(object):
    # TIMEOUT
    # def minPathSumDFS(self, grid):
    #     """
    #     :type grid: List[List[int]]
    #     :rtype: int
    #     """
    #     min_sum = 2**31 - 1
    #     dest_row = len(grid) - 1
    #     dest_col = len(grid[0]) - 1
    #     queue = [(0,0, grid[0][0])]
    #
    #     while len(queue) > 0:
    #         current_row, current_col, current_cost = queue.pop()
    #
    #         if current_row == dest_row and current_col == dest_col:
    #             if min_sum > current_cost:
    #                 min_sum = current_cost
    #
    #         neighbors = self.getNeighbors((current_row, current_col), grid)
    #         for neighbor in neighbors:
    #             neighbor[2] += current_cost
    #             queue.append(tuple(neighbor))
    #
    #     return min_sum
    def minPathSum(self, grid):
        memo = [[-1] * len(grid[0]) for i in range(len(grid))]
        self.helper(grid, 0,0, memo)

        return memo[0][0]

    def helper(self, grid, row, col, memo):
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            memo[row][col] = grid[row][col]
            return grid[row][col]
        if memo[row][col] != -1:
            return memo[row][col]

        neighbors = self.getNeighbors((row, col), grid)

        current_min = 2**31
        for neighbor in neighbors:
            current_neighbor_min = grid[row][col] + self.helper(grid, neighbor[0], neighbor[1], memo)
            if current_min > current_neighbor_min:
                current_min = current_neighbor_min

        memo[row][col] = current_min

        return current_min


    def getNeighbors(self, point, grid):
        neighbors = []

        # move right and down only
        right_col = point[1] + 1
        if right_col < len(grid[0]):
            neighbors.append([point[0], right_col])

        lower_row = point[0] + 1
        if lower_row < len(grid):
            neighbors.append([lower_row, point[1]])

        return neighbors

grid = [
    [7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],
    [9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],
    [8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],
    [6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],
    [7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],
    [9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],
    [1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],
    [3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],
    [1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],
    [5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],
    [2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],
    [0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]
]

# grid = [
#     [1,3,1],
#     [1,5,1],
#     [4,2,1]
# ]

solution = Solution()

print(solution.minPathSum(grid))
