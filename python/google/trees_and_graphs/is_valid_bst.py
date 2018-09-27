"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
"""

class Solution:
    def isValidBST(self, root):
        return self.helper(root, -4294967296, 4294967296)

    def helper(self, root, min, max):
        if root is None:
            return True

        if root.val <= min or root.val >= max:
            return False

        return self.helper(root.left, min, root.val) and self.helper(root.right, root.val, max)

