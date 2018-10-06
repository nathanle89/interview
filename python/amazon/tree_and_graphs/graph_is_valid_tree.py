# This problem is equivalent to detecting a cycle in an undirected graph

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) == 0 and n == 1:
            return True
        if len(edges) == 0 and n > 0:
            return False
        if len(edges) == 0 and n == 0:
            return True


        graph = {}
        root = edges[0][0]
        for edge in edges:
            if edge[0] in graph:
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]

            if edge[1] in graph:
                graph[edge[1]].append(edge[0])
            else:
                graph[edge[1]] = [edge[0]]

        visited = set()
        stack = [(root, None)]
        while len(stack) > 0:
            current, parent = stack.pop()
            visited.add(current)
            neighbors = graph[current]

            for neighbor in neighbors:
                if neighbor != parent:
                    stack.append((neighbor, current))
                    if neighbor in visited:
                        return False

        if len(visited) != n:
            return False

        return True

solution = Solution()
n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]

n2 = 5
edges2 = [[0,1], [1,2], [2,3], [1,3], [1,4]]

print solution.validTree(n, edges)
print solution.validTree(n2, edges2)
