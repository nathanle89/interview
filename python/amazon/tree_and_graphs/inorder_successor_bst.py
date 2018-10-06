# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        inorder = []
        successor = None
        self.inorderHelper(root, inorder)
        for i in range(len(inorder)):
            if inorder[i].val == p.val and i + 1 < len(inorder):
                successor = inorder[i+1]

        return successor

    def inorderHelper(self, root, inorder):
        if root is None:
            return

        self.inorderHelper(root.left, inorder)
        inorder.append(root)
        self.inorderHelper(root.right, inorder)


    def inorderSuccessorBST(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ
