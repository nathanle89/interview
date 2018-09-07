"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.global_counter = 0
        self.helper(root)
        return self.global_counter

    def helper(self, root):
        if root is None:
            return 0,

        left = self.helper(root.left)
        right = self.helper(root.right)
        tempLeft = 0
        tempRight = 0
        if root.left and root.right and root.val == root.left.val and root.val == root.right.val:
            tempLeft = left + 1
            tempRight = right + 1
        elif root.left and root.left.val == root.val:
            tempLeft += left + 1
        elif root.right and root.right.val == root.val:
            tempRight += right + 1

        self.global_counter = max([self.global_counter, tempLeft + tempRight])

        return max([tempLeft, tempRight])

node1 = TreeNode(6)
node2 = TreeNode(6)
node3 = TreeNode(6)
node4 = TreeNode(6)
node5 = TreeNode(6)
node6 = TreeNode(6)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.right = node6

solution = Solution()
print solution.longestUnivaluePath(node1)

