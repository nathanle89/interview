# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        all_leaves = []

        queue = [(root, None)]
        while len(queue) > 0:
            current, parent = queue.pop(0)

            if current.left is None and current.right is None:
                all_leaves.append((current, parent))

            if current.left:
                queue.append((current.left, (current, parent)))
            if current.right:
                queue.append((current.right, (current, parent)))
        sum = 0
        for leaf in all_leaves:
            sum += self.numberHelper(leaf)
        return sum

    def numberHelper(self, leaf):
        string_val = ''
        tmp = leaf
        while tmp:
            string_val += str(tmp[0].val)
            tmp = tmp[1]

        return int(string_val[::-1])
