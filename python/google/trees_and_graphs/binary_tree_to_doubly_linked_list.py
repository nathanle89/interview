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
        if root is None:
            return root

        list_left = self.flatten(root.left)
        list_right = self.flatten(root.right)
        root.left = None
        root.right = None

        list_left = self.concatinate(list_left, root)
        list_left = self.concatinate(list_left, list_right)

        return list_left

    def concatinate(self, list_a, list_b):
        if list_a is None:
            return list_b
        if list_b is None:
            return list_a

        # Traverse to the end of the list
        end_list_a = list_a
        while end_list_a.right is not None:
            end_list_a = end_list_a.right

        end_list_a.right = list_b
        list_b.left = end_list_a

        return list_a

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
result = solution.flatten(node1)
tmp = result
while tmp is not None:
    print tmp.val
    tmp = tmp.right
i = 0