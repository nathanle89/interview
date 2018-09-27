# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pathToP = self.pathToNode(root, p)
        pathToQ = self.pathToNode(root, q)

        length_path_P = len(pathToP)
        length_path_Q = len(pathToQ)

        if len(pathToP) > 0 and len(pathToQ) > 0:
            p_index = 0
            q_index = 0
            value = None
            while p_index < length_path_P and q_index < length_path_Q:
                if pathToP[p_index].val == pathToQ[q_index].val:
                    value = pathToP[p_index]
                else:
                    break
                p_index += 1
                q_index += 1

            return value
        else:
            return None

    def pathToNode(self, root, node):

        queue = [(root, [root])]

        while len(queue) > 0:
            currentNode, currentPath = queue.pop(0)

            if currentNode.val == node.val:
                return currentPath

            if currentNode.left:
                new_path = list(currentPath)
                new_path.append(currentNode.left)
                queue.append((currentNode.left, new_path))

            if currentNode.right:
                new_path = list(currentPath)
                new_path.append(currentNode.right)
                queue.append((currentNode.right, new_path))

        return []

class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root == p or root == q:
            return root

        left_result = self.lowestCommonAncestor(root.left, p, q)
        right_result = self.lowestCommonAncestor(root.right, p, q)

        if left_result and right_result:
            return root
        else:
            return left_result or right_result




node1 = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(1)
node4 = TreeNode(6)
node5 = TreeNode(2)
node6 = TreeNode(0)
node7 = TreeNode(8)
node8 = TreeNode(7)
node9 = TreeNode(4)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

node5.left = node8
node5.right = node9

solution = Solution()
print solution.lowestCommonAncestor(node1, node2, node9).val