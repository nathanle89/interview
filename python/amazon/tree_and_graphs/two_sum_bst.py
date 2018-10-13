# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        seen_num = set()
        queue = [root]

        while len(queue) > 0:
            current = queue.pop()

            if k - current.val in seen_num:
                return True

            seen_num.add(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return False
