"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []

        stack = [(root, None)]
        results = []
        while len(stack) > 0:
            current_node, parent = stack.pop()
            if current_node.left is None and current_node.right is None:
                results.append((current_node, parent))
            if current_node.left:
                stack.append((current_node.left, (current_node, parent)))
            if current_node.right:
                stack.append((current_node.right, (current_node, parent)))
        string_result = []
        for leaf_node in results:
            output = ""

            while leaf_node[1] is not None:
                output = "->" + str(leaf_node[0].val) + output
                leaf_node = leaf_node[1]
            output = str(leaf_node[0].val) + output
            string_result.append(output)

        return string_result

