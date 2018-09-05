# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.visit = root


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.visit is not None or len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        # Push things into the stack
        while self.visit is not None:
            self.stack.append(self.visit)
            self.visit = self.visit.left

        node = self.stack.pop()
        self.visit = node.right
        return node.val

        # Your BSTIterator will be called like this:
        # i, v = BSTIterator(root), []
        # while i.hasNext(): v.append(i.next())