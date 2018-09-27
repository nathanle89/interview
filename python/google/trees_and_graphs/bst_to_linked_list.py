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

    def flatten(self, root):
        self.helper(root, None)

    def helper(self, root, next_node):
        # we want to do preorder traversal
        if root is None:
            return

        if root.left is None and root.right is None:
            root.right = next_node
            return

        left = root.left
        right = root.right
        root.left = None
        if left is not None:
            root.right = left

        if right is None:
            right = next_node
            self.helper(left, right)
        else:
            self.helper(left, right)
            self.helper(right, next_node)

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.right = node5

node2.left = node3
node2.right = node4

node5.right = node6

solution = Solution()
print(solution.flatten(node1))
print(solution.preorderTraversal(node1))
