# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        queue = [(root, 0)]
        results = []
        current_level = []
        current_level_id = 0
        while len(queue) > 0:
            current = queue.pop(0)
            if current[1] != current_level_id:
                results.append(current_level)
                current_level_id = current[1]
                current_level = [current[0].val]
            else:
                current_level.append(current[0].val)

            if current[0].left is not None:
                queue.append((current[0].left, current[1] + 1))
            if current[0].right is not None:
                queue.append((current[0].right, current[1] + 1))

            if len(queue) == 0 and len(current_level) > 0:
                results.append(current_level)

        return results
