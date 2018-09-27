
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None

        leftNode = self.treeToDoublyList(root.left)
        rightNode = self.treeToDoublyList(root.right)

        root.left = root
        root.right = root

        leftNode = self.circularLinkNodes(leftNode, root)
        leftNode = self.circularLinkNodes(leftNode, rightNode)

        return leftNode

    def circularLinkNodes(self, nodeA, nodeB):
        if nodeA is None:
            return nodeB
        if nodeB is None:
            return nodeA

        end_of_A = nodeA.left
        end_of_B = nodeB.left
        end_of_A.right = nodeB
        nodeA.left = end_of_B
        nodeB.left = end_of_A
        end_of_B.right = nodeA

        return nodeA

node1 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(5)
node4 = TreeNode(1)
node5 = TreeNode(3)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

solution = Solution()

result = solution.treeToDoublyList(node1)
i = 0
