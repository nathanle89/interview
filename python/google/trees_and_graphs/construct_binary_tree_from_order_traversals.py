"""

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(preorder, inorder)

    def helper(self, preorder, inorder):
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        preorder_index, inorder_index = self.findRootIndex(preorder, inorder)
        root = TreeNode(preorder[preorder_index])

        left_subtree_preorder = preorder[preorder_index+1:inorder_index+1]
        left_subtree_inorder = inorder[0:inorder_index]

        right_subtree_preorder = preorder[inorder_index+1:]
        right_subtree_inorder = inorder[inorder_index+1:]

        root.left = self.helper(left_subtree_preorder, left_subtree_inorder)
        root.right = self.helper(right_subtree_preorder, right_subtree_inorder)

        return root

    def findRootIndex(self, preorder, inorder):
        preorder_index = 0
        inorder_index = 0

        for i in range(len(inorder)):
            if inorder[i] == preorder[preorder_index]:
                inorder_index = i
                break

        return preorder_index, inorder_index

solution = Solution()

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
out = solution.buildTree(preorder, inorder)
i = 0