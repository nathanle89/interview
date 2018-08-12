class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return

        print root.val
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

    def sortedArrayToBST(self, nums):
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, lower, upper):
        if lower > upper:
            return None
        if lower == upper:
            return TreeNode(nums[lower])

        mid = int(round((lower + upper)/2.))

        root = TreeNode(nums[mid])
        root.left = self.helper(nums, lower, mid - 1)
        root.right = self.helper(nums, mid+1, upper)

        return root

nums = [-10,-3,0,5,9]

solution = Solution()
tree = solution.sortedArrayToBST(nums)

solution.preorderTraversal(tree)
