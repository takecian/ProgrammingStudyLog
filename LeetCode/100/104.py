# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def count(node, depth):
            if not node:
                return depth
            return max(count(node.left, depth + 1), count(node.right, depth + 1))

        return count(root, 0)