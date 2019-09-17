# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_mirror(lnode, rnode):
            if lnode is None and rnode is None:
                return True
            if lnode is None or rnode is None:
                return False
            if lnode.val != rnode.val:
                return False
            return is_mirror(lnode.left, rnode.right) and is_mirror(lnode.right, rnode.left)
        return is_mirror(root, root)