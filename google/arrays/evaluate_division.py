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

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        results = {}
        variable_set = set()
        for i in range(len(equations) - 1):
            equation1 = equations[i]
            value1 = values[i]
            results[equation1[0] + equation1[1]] = value1
            results[equation1[1] + equation1[0]] = 1./value1
            variable_set.add(equation1[0])
            variable_set.add(equation1[1])
            for j in range(i + 1, len(equations)):
                equation2 = equations[j]
                value2 = values[j]
                results[equation2[0] + equation2[1]] = value2
                variable_set.add(equation2[0])
                variable_set.add(equation2[1])
                if equation1[0] == equation2[1]:
                    results[equation2[0] + equation1[1]] = value1 * value2
                if equation1[1] == equation2[0]:
                    results[equation1[0] + equation2[1]] = value1 * value2
                if equation1[0] == equation2[0]:
                    results[equation2[1] + equation1[1]] = value1 * 1./value2
                    results[equation1[1] + equation2[1]] = 1./value1 * value2
                if equation1[1] == equation2[1]:
                    results[equation2[0] + equation1[0]] = 1./value1 * value2
                    results[equation1[0] + equation2[0]] = value1 * 1./value2

        out = []
        for query in queries:
            key = query[0] + query[1]
            if query[0] not in variable_set or query[1] not in variable_set:
                out.append(-1.0)
            elif query[0] == query[1]:
                out.append(1.0)
            elif key in results:
                out.append(results[key])
            else:
                out.append(-1.0)

        return out

solution = Solution()

print(solution.calcEquation([ ["a", "b"], ["b", "c"] ], [2.0, 3.0], [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]))
