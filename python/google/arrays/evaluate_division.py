"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""

class Pair(object):
    def __init__(self, dividend, value):
        self.dividend = dividend
        self.value = value

class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = {}

        # Build graph from input equations
        for i in range(len(equations)):
            equation = equations[i]
            value = values[i]

            if equation[0] not in graph:
                graph[equation[0]] = []
            if equation[1] not in graph:
                graph[equation[1]] = []

            graph[equation[0]].append(Pair(equation[1], value))
            graph[equation[1]].append(Pair(equation[0], 1.0/value))

        # Answering queries by using BFS
        results = []
        for query in queries:
            start = query[0]
            end = query[1]

            results.append(self.bfs(start, end, graph))

        return results

    def bfs(self, start, end, graph):
        queue = [(start, 1.0)]
        visited = set([start])
        if start not in graph or end not in graph:
            return -1.0

        while len(queue) > 0:
            current_node, value = queue.pop(0)

            if current_node == end:
                return value

            neighbors = graph[current_node]
            for neighbor in neighbors:
                if neighbor.dividend in visited:
                    continue
                visited.add(neighbor.dividend)
                queue.append((neighbor.dividend, value * neighbor.value))

        return -1.0

solution = Solution()

print(solution.calcEquation([ ["a", "b"], ["b", "c"] ], [2.0, 3.0], [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]))
