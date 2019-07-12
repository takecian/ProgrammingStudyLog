# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        self.flatten(root.right)
        self.flatten(root.left)

        if root.left is not None:
            cursor = root.left
            while cursor.right:
                if cursor.right is not None:
                    cursor = cursor.right
            cursor.right = root.right

            root.right = root.left
            root.left = None

        return
