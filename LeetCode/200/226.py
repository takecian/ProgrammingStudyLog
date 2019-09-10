# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(node):
            if node is None:
                return
            node.left, node.right = node.right, node.left
            invert(node.left)
            invert(node.right)

        invert(root)
        return root
