"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

Example 1:

Input: root = [2,1,3], p = 1

  2
 / \
1   3

Output: 2
Example 2:

Input: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /
1

Output: null
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        array = []
        self.helper(root, array)
        result_index = -1
        for i in range(len(array)):
            node = array[i]
            if p.val == node.val:
                result_index = i
                break

        if result_index > -1 and result_index + 1 < len(array):
            return array[result_index + 1]
        return None

    def helper(self, root, array):
        if root is None:
            return None

        self.helper(root.left, array)
        array.append(root)
        self.helper(root.right, array)


node1 = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)

node1.left = node2
node1.right = node3

solution = Solution()
print solution.inorderSuccessor(node1, node2)