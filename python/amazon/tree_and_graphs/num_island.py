class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island_counter = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    self.dfs(grid, (i, j), visited)
                    island_counter += 1

        return island_counter

    def dfs(self, grid, start, visited):
        stack = [start]

        while len(stack) > 0:
            current = stack.pop()

            neighbors = self.getNeighbors(grid, current)
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

    def getNeighbors(self, grid, current):
        neightbors = []
        if current[0] - 1 >= 0 and grid[current[0] - 1][current[1]] == '1':
            neightbors.append((current[0] - 1, current[1]))
        if current[0] + 1 < len(grid) and grid[current[0] + 1][current[1]] == '1':
            neightbors.append((current[0] + 1, current[1]))
        if current[1] - 1 >= 0 and grid[current[0]][current[1] - 1] == '1':
            neightbors.append((current[0], current[1] - 1))
        if current[1] + 1 < len(grid[0]) and grid[current[0]][current[1] + 1] == '1':
            neightbors.append((current[0], current[1] + 1))

        return neightbors


solution = Solution()
grid = [
    list('11110'),
    list('11010'),
    list('11000'),
    list('00000')
]
print solution.numIslands(grid)
