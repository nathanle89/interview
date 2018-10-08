# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    # This uses string preorder serialization
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        serialized_s = self.serialize(s)
        serialized_t = self.serialize(t)
        return serialized_t in serialized_s

    def serialize(self, tree):
        encode = []
        self.serializeHelper(tree, encode)
        return ''.join(encode)

    def serializeHelper(self, s, encode):
        if s is None:
            encode.append('*')
            return

        encode.append('#' + str(s.val))
        self.serializeHelper(s.left, encode)
        self.serializeHelper(s.right, encode)


    # SLOW AS SHIT
    def isSubtree2(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        #do bfs
        queue = [s]
        while len(queue) > 0:
            current = queue.pop(0)

            if current.val == t.val and self.checker(current, t):
                return True
            else:
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)

        return False


    def checker(self, s, t):
        if s is None and t is None:
            return True

        if s is None and t is not None:
            return False

        if s.val != t.val:
            return self.checker(s.left, t) or self.checker(s.right, t)
        else:
            # Found a matching starting point
            return self.helper(s, t)

    def helper(self, s, t):
        if s is None and t is not None:
            return False

        if s is not None and t is None:
            return False

        if s is None and t is None:
            return True

        if s.val != t.val:
            return False

        return self.helper(s.left, t.left) and self.helper(s.right, t.right)

s = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)
node3 = TreeNode(1)
node4 = TreeNode(2)
node5 = TreeNode(0)
s.left = node1
s.right = node2
node1.left = node3
node1.right = node4
node4.right = node5

t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)

solution = Solution()
solution.isSubtree2(s, t)
