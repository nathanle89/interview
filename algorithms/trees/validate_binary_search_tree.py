# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, -4294967296, 4294967296)

    def helper(self, root, min, max):
        if root is None:
            return True

        if root.val < min or root.val > max:
            return False

        return self.helper(root.left, min, root.val - 1) and self.helper(root.left, root.val + 1, max)
