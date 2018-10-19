
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = set()
        circle_counter = 0

        #build a graph
        graph = {}

        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1 and i != j:
                    if i in graph:
                        graph[i].append(j)
                    else:
                        graph[i] = [j]

        for i in range(len(M)):
            if i not in visited:
                self.dfs(graph, i, visited)
                circle_counter += 1

        return circle_counter

    def dfs(self, graph, source, visited):
        stack = [source]

        while len(stack) > 0:
            current = stack.pop()

            if current in graph:
                neighbors = graph[current]
            else:
                neighbors = []

            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

M = [
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,1,1]
]

M2 = [[1,1,0],
      [1,1,0],
      [0,0,1]]

M3 = [[1,1,0],
     [1,1,1],
     [0,1,1]]

solution = Solution()
assert(solution.findCircleNum(M) == 1)
assert(solution.findCircleNum(M2) == 2)
assert(solution.findCircleNum(M3) == 1)
