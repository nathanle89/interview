"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        preorder_p = self.preorderTraversal(p)
        preorder_q = self.preorderTraversal(q)
        return preorder_p == preorder_q

    def preorderTraversal(self, root):
        array = []
        self.helper(root, array)
        return array

    def helper(self, root, array):
        if root is None:
            array.append(None)
            return

        array.append(root.val)
        self.helper(root.left, array)
        self.helper(root.right, array)
