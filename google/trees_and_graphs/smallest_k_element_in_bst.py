"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 <= k <= BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        array = []
        self.inorderTraversal(root, array, k)
        return array[-1]

    def inorderTraversal(self, root, array, k):
        if root is None:
            return

        if len(array) < k:
            self.inorderTraversal(root.left, array, k)
        if len(array) < k:
            array.append(root.val)
        if len(array) < k:
            self.inorderTraversal(root.right, array, k)

node1 = TreeNode(3)
node2 = TreeNode(1)
node3 = TreeNode(4)
node4 = TreeNode(2)

node1.left = node2
node1.right = node3
node2.right = node4

solution = Solution()
print solution.kthSmallest(node1, 1)
