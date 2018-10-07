class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = {}
        graph[words[0][0]] = []
        for word in words:
            graph.append()
