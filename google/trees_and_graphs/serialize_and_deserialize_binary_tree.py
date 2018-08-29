"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        array = []
        self.preorderTraversal(root, array)
        return array

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        index = 0
        result, current_index = self.deserializeHelper(data, index)
        return result

    def deserializeHelper(self, data, index):

        if index >= len(data) or data[index] == '-1':
            return (None, index+1)

        root = TreeNode(data[index])
        index += 1

        left_node, current_index = self.deserializeHelper(data, index)
        right_node, current_index = self.deserializeHelper(data, current_index)

        root.left = left_node
        root.right = right_node

        return (root, current_index)


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))
    def preorderTraversal(self, root, array):
        if root is None:
            array.append('-1')
            return

        array.append(root.val)
        self.preorderTraversal(root.left, array)
        self.preorderTraversal(root.right, array)

node1 = TreeNode(7)
node2 = TreeNode(2)
node3 = TreeNode(5)
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(8)

node1.left = node2
node1.right = node3

node2.left = node4

node3.left = node5
node3.right = node6

solution = Codec()
serialized_result = solution.serialize(node1)
print serialized_result
deserialized_tree = solution.deserialize(serialized_result)
i = 0
