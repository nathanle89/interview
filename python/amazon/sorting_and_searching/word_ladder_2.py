# class Solution(object):
#     def findLadders(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: List[List[str]]
#         """
#         if endWord not in wordList:
#             return []
#
#         # Build the graph
#         graph = {}
#
#         copied = list(wordList)
#         copied.extend([beginWord, endWord])
#         for word in copied:
#             for i in range(len(word)):
#                 graph_vertex = str(word[:i]) + '*' + str(word[i+1:])
#                 if graph_vertex in graph:
#                     graph[graph_vertex].append(word)
#                 else:
#                     graph[graph_vertex] = [word]
#
#         queue = [(beginWord, [beginWord], set([beginWord]))]
#         # visited = set()
#         # visited.add(beginWord)
#         min_length = None
#         results = []
#         while len(queue) > 0:
#             current_vertex, path, visited = queue.pop(0)
#
#             if current_vertex == endWord:
#                 if min_length is not None and len(path) > min_length:
#                     break
#
#                 if ((len(path) == min_length) or min_length is None):
#                     results.append(path)
#                 min_length = len(path)
#             else:
#                 # Get Neighbors
#                 for i in range(len(current_vertex)):
#                     graph_vertex = str(current_vertex[:i]) + '*' + str(current_vertex[i+1:])
#                     if graph_vertex in graph:
#                         potential_neighbors = graph[graph_vertex]
#                         for neighbor in potential_neighbors:
#                             if neighbor not in visited:
#                                 copied_path = list(path)
#                                 copied_path.append(neighbor)
#                                 copied_visited = set(visited)
#                                 copied_visited.add(neighbor)
#                                 queue.append((neighbor, copied_path, copied_visited))
# 
#
#         return results

# solution = Solution()
#
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# print solution.findLadders(beginWord, endWord, wordList)
