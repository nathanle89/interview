class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        # Build the graph
        graph = {}

        copied = list(wordList)
        copied.extend([beginWord, endWord])
        for word in copied:
            for i in range(len(word)):
                graph_vertex = str(word[:i]) + '*' + str(word[i+1:])
                if graph_vertex in graph:
                    graph[graph_vertex].append(word)
                else:
                    graph[graph_vertex] = [word]

        queue = [(beginWord, 1)]
        visited = set()
        visited.add(beginWord)

        while len(queue) > 0:
            current_word, counter = queue.pop(0)

            if current_word == endWord:
                return counter

            # Get Neighbors
            for i in range(len(current_word)):
                graph_vertex = str(current_word[:i]) + '*' + str(current_word[i+1:])
                if graph_vertex in graph:
                    potential_neighbors = graph[graph_vertex]
                    for neighbor in potential_neighbors:
                        if neighbor not in visited:
                            queue.append((neighbor, counter + 1))
                            visited.add(neighbor)

        return 0

solution = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print solution.ladderLength(beginWord, endWord, wordList)
