# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def printTreeByLevel(self, root):
        if root is None:
            return

        currentLevel = 0

        # BFS
        queue = [(root, 0)]
        current_level_element = []
        while len(queue) > 0:
            current_node, level = queue.pop(0)
            if level == currentLevel:
                current_level_element.append(current_node.val)
            else:
                print(current_level_element)
                current_level_element = [current_node.val]
                currentLevel = level

            if current_node.left is not None:
                queue.append((current_node.left, level + 1))

            if current_node.right is not None:
                queue.append((current_node.right, level + 1))

            if len(queue) == 0:
                print(current_level_element)


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
solution.printTreeByLevel(node1)