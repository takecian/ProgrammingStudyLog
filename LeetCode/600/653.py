# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None:
            return False
        que = [root]
        expected = set()
        while que:
            node = que.pop(0)
            if node.val in expected:
                return True

            expected.add(k - node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)

        return False
