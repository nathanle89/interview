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
        if root is None:
            return ""

        array = []
        self.serializeHelper(root, array)
        return "#".join(array)

    def serializeHelper(self, root, array):
        if root is None:
            array.append('*')
            return

        array.append(str(root.val))
        self.serializeHelper(root.left, array)
        self.serializeHelper(root.right, array)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0 or data is None:
            return None

        self.counter = 0
        vals = data.split('#')
        root = self.deserializeHelper(vals)
        return root

    def deserializeHelper(self, values):
        if values[self.counter] == '*':
            self.counter += 1
            return None

        root = TreeNode(values[self.counter])
        self.counter += 1

        root.left = self.deserializeHelper(values)
        root.right = self.deserializeHelper(values)

        return root

    # Your Codec object will be instantiated and called as such:

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.left = node1
root.right = node2

node3 = TreeNode(4)
node4 = TreeNode(5)
node2.left = node3
node2.right = node4


codec = Codec()
codec.deserialize(codec.serialize(root))
