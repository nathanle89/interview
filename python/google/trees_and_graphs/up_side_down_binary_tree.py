class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        post_order = self.postOrderTraversal(root)
        # move the first 2 None to the end
        del post_order[1]
        del post_order[1]
        post_order.append(None)
        post_order.append(None)

        return self.deserialize(post_order)

    def deserialize(self, preorder):
        index = 0
        root, current_index = self.deserializeHelper(preorder, index)
        return root

    def deserializeHelper(self, preorder, index):
        if index == len(preorder) or preorder[index] is None:
            return (None, index + 1)

        root = TreeNode(preorder[index])
        index += 1

        left_node, current_index = self.deserializeHelper(preorder, index)
        root.left = left_node
        right_node, current_index = self.deserializeHelper(preorder, current_index)
        root.right = right_node

        return root, current_index

    def postOrderTraversal(self, root):
        array = []
        self.helper(root, array)
        return array

    def helper(self, root, array):
        if root is None:
            array.append(None)
            return

        self.helper(root.left, array)
        self.helper(root.right, array)
        array.append(root.val)