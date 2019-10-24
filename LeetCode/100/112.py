# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        def has_sum(node, total, target):
            if not node:
                return False
            if node.left is None and node.right is None:
                if total + node.val == target:
                    return True
                else:
                    return False

            return has_sum(node.left, total + node.val, target) or has_sum(node.right, total + node.val, target)

        return has_sum(root, 0, sum)