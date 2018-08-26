"""
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 <= k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y

Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]
"""
#
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_word = False
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word):
#         current = self.root
#
#         for i in range(0, len(word)):
#             char = word[i]
#
#             if char not in current.children:
#                 new_char_node = TrieNode()
#                 current.children[char] = new_char_node
#             else:
#                 new_char_node = current.children[char]
#
#             current = new_char_node
#
#         current.is_end_word = True
#
#     def bfs_char(self):
#         queue = [(self.root, 1)]
#         result = []
#         current_level_char_map = set()
#         current_level = 1
#         while len(queue) > 0:
#             current_node, level = queue.pop(0)
#
#             for key, val in current_node.children.iteritems():
#                 queue.append((val, level + 1))
#
#             if current_level != level:
#                 result.append(current_level_char_map)
#                 current_level_char_map = set()
#                 current_level = level
#
#             # Collecting all char for the given node
#             current_level_char_map.update(current_node.children.keys())
#
#             if len(queue) == 0 and len(current_level_char_map) > 0:
#                 result.append(current_level_char_map)
#
#         return result
#
#     def search_by_prefix(self, prefix):
#
#
#
#
# class Solution(object):
#     def wordSquares(self, words):
#         """
#         :type words: List[str]
#         :rtype: List[List[str]]
#         """
#         # Build the Trie for all existing words
#         # O(l * n)
#         trie = Trie()
#         for word in words:
#             trie.insert(word)
#
#         char_map_by_level = trie.bfs_char()
#
#         group_words_by_level = []
#         for level_char in char_map_by_level:
#             words_level = []
#
#             for word in words:
#                 word_set = set(word)
#                 if word_set.issubset(level_char):
#                     words_level.append(word)
#             group_words_by_level.append(words_level)
#
#         results = []
#
#         for i in range(0, len(group_words_by_level)):
#             word_level = group_words_by_level[i]
#
#             if i == 0:
#                 for each_word in word_level:
#                     results.append([each_word])
#             else:
#                 for each_result_group in results:
#                     for each_word in words_level:
#                         each_result_group.append(each_word)
#
#
#
#
#         i = 0

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        trie = {}
        self.build_trie(words, trie)

        size = len(words[0])

        result = []
        self.find_word_squares(trie, size, [], result)
        return result

    def build_trie(self, words, trie):
        for word in words:
            self.add_str(word, trie)

    def add_str(self, string, root):
        node = root
        for letter in string:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['#'] = string

    def search_prefix(self, node, prefix, candidates):
        if '#' in node:
            candidates.append(node['#'])
            return

        for letter in prefix:
            if letter not in node:
                return
            node = node[letter]

        for letter in node:
            self.search_prefix(node[letter], '', candidates)

    def find_word_squares(self, trie, size, cur, result):
        if len(cur) == size:
            result.append(cur[:])
            return

        candidates = []
        prefix = ''.join([string[len(cur)] for string in cur])
        self.search_prefix(trie, prefix, candidates)

        for candidate in candidates:
            self.find_word_squares(trie, size, cur + [candidate], result)



solution = Solution()

solution.wordSquares(["ball","area","lead","lady"])
# solution.wordSquares(["area","lead","wall","lady","ball"])
# solution.wordSquares(["abat","baba","atan","atal"])

i = 0
