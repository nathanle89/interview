# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        max_left = self.maxDepth(root.left) + 1
        max_right = self.maxDepth(root.right) + 1

        return max([max_left, max_right])

node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node1.left = node2
node1.right = node3

node3.left = node4
node3.right = node5

solution = Solution()
print(solution.maxDepth(node1))

