# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = -10 ** 10

        def rec(node):
            nonlocal ans
            if node is None:
                return 0
            ans = max(ans, node.val)

            right = rec(node.right)
            left = rec(node.left)
            ans = max(ans, node.val + max(0, right) + max(0, left))
            return node.val + max(0, left, right)

        rec(root)
        return ans