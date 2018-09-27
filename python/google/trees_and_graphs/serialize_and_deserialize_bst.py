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
        str_mapper = lambda x: str(x)
        return "#".join(map(str_mapper, array))


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None

        int_mapper = lambda x: int(x)
        input_data = map(int_mapper, data.split('#'))
        pivot, left, right = self.partitionData(input_data)
        return self.deserializeHelper(pivot, left, right)

    def deserializeHelper(self, pivot, left, right):
        if (len(left) == 0 and len(right) == 0):
            if pivot is None:
                return None
            else:
                return TreeNode(pivot)

        root = TreeNode(pivot)

        pivot_sub, left_sub, right_sub = self.partitionData(left)
        root.left = self.deserializeHelper(pivot_sub, left_sub, right_sub)

        pivot_sub, left_sub, right_sub = self.partitionData(right)
        root.right = self.deserializeHelper(pivot_sub, left_sub, right_sub)

        return root

    def partitionData(self, array):
        if len(array) == 0:
            return (None, [], [])

        pivot = array[0]
        left = []
        right = []
        for i in range(1, len(array)):
            if array[i] < pivot:
                left.append(array[i])
            else:
                right.append(array[i])
        return (pivot, left, right)

    def preorderTraversal(self, root, array):
        if root is None:
            return

        array.append(root.val)
        self.preorderTraversal(root.left, array)
        self.preorderTraversal(root.right, array)

node1 = TreeNode(5)
node2 = TreeNode(2)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(4)
node6 = TreeNode(7)
node7 = TreeNode(6)
node8 = TreeNode(8)

node1.left = node2
node1.right = node6

node2.left = node3
node2.right = node4

node4.right = node5

node6.left = node7
node6.right = node8

codec = Codec()
data = codec.serialize(node1)
print data
root = codec.deserialize(data)
i = 0
