# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if root is None:
            return None, None

        if root.val <= V:
            lte, gt = self.splitBST(root.right, V)
            root.right = lte
            return root, gt
        else:
            lte, gt = self.splitBST(root.left, V)
            root.left = gt
            return lte, root
