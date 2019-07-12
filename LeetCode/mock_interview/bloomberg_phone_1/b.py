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

        right = self.solve(root.right)
        left = self.solve(root.left)

        if left is not None:
            root.right = left
            cursor = root.right
            while cursor.right:
                if cursor.right is not None:
                    cursor = cursor.right
            cursor.right = right
        else:
            root.right = right
        root.left = None

        return

    def solve(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        right = self.solve(root.right)
        left = self.solve(root.left)

        if left is not None:
            root.right = left
            cursor = root.right
            while cursor.right:
                if cursor.right is not None:
                    cursor = cursor.right
            cursor.right = right
        else:
            root.right = right

        root.left = None

        return root
