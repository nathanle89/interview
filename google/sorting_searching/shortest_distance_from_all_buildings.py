"""
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
"""

class Solution(object):
    def shortestDistance(self, grid):

        row = len(grid)
        col = len(grid[0])
        total_houses = 0
        distance_matrix = []
        reach_matrix = []
        for i in range(row):
            distance_matrix.append([0] * col)
            reach_matrix.append([0] * col)

        # BFS and populate distance_matrix as well as reach_matrix
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    self.bfs([i, j], distance_matrix, reach_matrix, grid)
                    total_houses += 1

        # Find the smallest cell that can reach all possible houses
        current_min_distance = 2**31 - 1
        for i in range(row):
            for j in range(col):
                if distance_matrix[i][j] > 0 and reach_matrix[i][j] == total_houses:
                    if current_min_distance > distance_matrix[i][j]:
                        current_min_distance = distance_matrix[i][j]

        if current_min_distance == 2**31 - 1:
            return -1
        else:
            return current_min_distance

    def bfs(self, source, distance_matrix, reach_matrix, grid):
        queue = [(source, 0)]
        visited = set()

        while len(queue) > 0:
            current_location, total_distance = queue.pop(0)

            distance_matrix[current_location[0]][current_location[1]] += total_distance
            reach_matrix[current_location[0]][current_location[1]] += 1

            neighbors = self.neighbors(current_location, grid)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, total_distance + 1))

    def neighbors(self, current_slot, grid):
        neighbors = []

        if current_slot[0] - 1 >= 0 and (grid[current_slot[0] - 1][current_slot[1]] == 0):
            neighbors.append((current_slot[0] - 1, current_slot[1]))

        if current_slot[1] - 1 >= 0 and (grid[current_slot[0]][current_slot[1] - 1] == 0):
            neighbors.append((current_slot[0], current_slot[1] - 1))

        if current_slot[1] + 1 < len(grid[0]) and (grid[current_slot[0]][current_slot[1] + 1] == 0):
            neighbors.append((current_slot[0], current_slot[1] + 1))

        if current_slot[0] + 1 < len(grid) and (grid[current_slot[0] + 1][current_slot[1]] == 0):
            neighbors.append((current_slot[0] + 1, current_slot[1]))

        return neighbors


grid = [[1,1],[0,1]]
solution = Solution()

print solution.shortestDistance(grid)