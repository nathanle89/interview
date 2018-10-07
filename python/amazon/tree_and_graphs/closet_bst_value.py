# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        current = root
        best_candidate = -1
        current_diff = 2**32

        # Figure this out
        while current:
            if abs(target - current.val) <= 0.5:
                return current.val
            else:
                if abs(current.val - target) < current_diff:
                    best_candidate = current.val
                    current_diff = abs(current.val - target)

                if target < current.val:
                    current = current.left
                else:
                    current = current.right

        return best_candidate
