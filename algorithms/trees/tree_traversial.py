# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return

        print root.val
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

    def inorderTraversal(self, root):
        if root is None:
            return

        self.inorderTraversal(root.left)
        print root.val
        self.inorderTraversal(root.right)

    def postorderTraveral(self, root):
        if root is None:
            return

        self.postorderTraveral(root.left)
        self.postorderTraveral(root.right)
        print root.val

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

solution = Solution()
solution.postorderTraveral(node1)