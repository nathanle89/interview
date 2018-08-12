class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True

        queue = [[root.left, root.right]]

        while len(queue) > 0:
            pair = queue.pop(0)
            left_node = pair[0]
            right_node = pair[1]

            if left_node is None and right_node is None:
                continue

            if left_node is None or right_node is None:
                return False

            if left_node.val != right_node.val:
                return False

            queue.append([left_node.left, right_node.right])
            queue.append([left_node.right, right_node.left])

        return True


node1 = TreeNode(9)
node2 = TreeNode(-42)
node3 = TreeNode(-42)
node4 = TreeNode(76)
node5 = TreeNode(76)
node6 = TreeNode(13)
node7 = TreeNode(13)

node1.left = node2
node1.right = node3

node2.right = node4
node3.left = node5

node4.right = node6
node5.right = node7

solution = Solution()
print(solution.isSymmetric(node1))