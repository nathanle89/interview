# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        queue = [(root, 0)]
        results = []

        while len(queue) > 0:
            current, tag = queue.pop(0)
            results.append((current.val, tag))

            if current.left is not None:
                queue.append((current.left, tag - 1))

            if current.right is not None:
                queue.append((current.right, tag + 1))

        # Combine step
        results_dict = {}
        for node in results:
            if node[1] in results_dict:
                results_dict[node[1]].append(node[0])
            else:
                results_dict[node[1]] = [node[0]]

        keys = results_dict.keys()
        keys.sort()
        final_result = []
        for key in keys:
            final_result.append(results_dict[key])

        return final_result
