"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:

Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
Examples 2:

Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
Examples 3:

Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        stack = [(root, 0)]
        vertical_order = {}

        #BFS
        while len(stack) > 0:
            current_node, horizontal_depth = stack.pop(0)

            if horizontal_depth in vertical_order:
                vertical_order[horizontal_depth].append(current_node.val)
            else:
                vertical_order[horizontal_depth] = [current_node.val]

            if current_node.left:
                stack.append((current_node.left, horizontal_depth - 1))

            if current_node.right:
                stack.append((current_node.right, horizontal_depth + 1))

        sorted_result = []
        for val, item in vertical_order.iteritems():
            sorted_result.append((val, item))

        sorted_result.sort()

        final_result = []
        for pair in sorted_result:
            final_result.append(pair[1])

        return final_result
