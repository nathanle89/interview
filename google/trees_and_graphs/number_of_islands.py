class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row_count = len(grid)
        if row_count == 0:
            return 0

        col_count = len(grid[0])

        visited = set()
        island_count = 0

        for i in range(0, row_count):
            for j in range(0, col_count):
                if grid[i][j] == '0':
                    continue
                elif (i, j) in visited:
                    continue
                else:
                    # BFS Style exploring
                    self.exploreBFS(i, j, grid, row_count, col_count, visited)
                    island_count += 1

        return island_count

    def exploreBFS(self, i, j, grid, row_length, col_length, visited):
        queue = [(i, j)]

        while len(queue) > 0:
            current_cell = queue.pop()

            unvisited_neighbors = self.getTraverseableNeighbors(current_cell[0], current_cell[1], grid, row_length, col_length, visited)

            for neighbor in unvisited_neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


    def getTraverseableNeighbors(self, i, j, grid, row_length, col_length, visited):
        neighbors = []
        top_neighbor_x, top_neighbor_y = i - 1, j
        left_neighbor_x, left_neighbor_y = i, j - 1
        right_neighbor_x, right_neighbor_y = i, j + 1
        bottom_neighbor_x, bottom_neighbor_y = i + 1, j

        if top_neighbor_x < row_length and top_neighbor_x >= 0 and top_neighbor_y >= 0 and top_neighbor_y < col_length and grid[top_neighbor_x][top_neighbor_y] == '1' and (top_neighbor_x, top_neighbor_y) not in visited:
            neighbors.append((top_neighbor_x, top_neighbor_y))

        if left_neighbor_x < row_length and left_neighbor_x >= 0 and left_neighbor_y >= 0 and left_neighbor_y < col_length and grid[left_neighbor_x][left_neighbor_y] == '1' and (left_neighbor_x, left_neighbor_y) not in visited:
            neighbors.append((left_neighbor_x, left_neighbor_y))

        if right_neighbor_x < row_length and right_neighbor_x >= 0 and right_neighbor_y >= 0 and right_neighbor_y < col_length and grid[right_neighbor_x][right_neighbor_y] == '1' and (right_neighbor_x, right_neighbor_y) not in visited:
            neighbors.append((right_neighbor_x, right_neighbor_y))

        if bottom_neighbor_x < row_length and bottom_neighbor_x >= 0 and bottom_neighbor_y >= 0 and bottom_neighbor_y < col_length and grid[bottom_neighbor_x][bottom_neighbor_y] == '1' and (bottom_neighbor_x, bottom_neighbor_y) not in visited:
            neighbors.append((bottom_neighbor_x, bottom_neighbor_y))

        return neighbors

solution= Solution()

input = [
    list('11000'),
    list('11000'),
    list('00100'),
    list('00011')
]

input2 = [
    list('11110'),
    list('11010'),
    list('11000'),
    list('00000')
]

input3 = [
    ["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
    ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
    ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
    ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
    ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]
]

print(solution.numIslands(input3))
