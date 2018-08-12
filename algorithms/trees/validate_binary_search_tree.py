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

    def helper(self, root, min_val, max_val):
        if root is None:
            return True

        if root.val < min_val or root.val > max_val:
            return False

        return self.helper(root.left, min_val, root.val-1) and self.helper(root.right, root.val+1, max_val)
