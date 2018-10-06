# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, 2**31 - 1, -2**31)

    def helper(self, root, max, min):
        if root is None:
            return True

        if root.val > max or root.val < min:
            return False

        return self.helper(root.left, root.val - 1, min) and self.helper(root.right, max, root.val + 1)
