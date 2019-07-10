# https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        return self.sufficientSubsetEx(root, limit, 0)

    def sufficientSubsetEx(self, root: TreeNode, limit: int, total: int) -> TreeNode:
        if root.left is None and root.right is None:
            s = total + root.val
            # print('{} {}'.format(root.val, s))
            if limit <= s:
                return root
            else:
                return None
        else:
            if root.left:
                root.left = self.sufficientSubsetEx(root.left, limit, total + root.val)

            if root.right:
                root.right = self.sufficientSubsetEx(root.right, limit, total + root.val)

            if root.left is None and root.right is None:
                return None
        return root