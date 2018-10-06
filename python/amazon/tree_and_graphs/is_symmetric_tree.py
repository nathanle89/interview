# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        queue = [[root.left, root.right]]

        while len(queue) > 0:
            current = queue.pop(0)

            if current[0] is not None and current[1] is None:
                return False

            if current[0] is None and current[1] is not None:
                return False

            if current[0] is not None and current[1] is not None:
                if current[0].val != current[1].val:
                    return False

                queue.append([current[0].left, current[1].right])
                queue.append([current[0].right, current[1].left])

        return True

solution = Solution()
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(4)
node6 = TreeNode(3)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6

print solution.isSymmetric(root)
