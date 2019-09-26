# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node.left:
                nodes.append((node.left, 2 * v))
            if node.right:
                nodes.append((node.right, 2 * v + 1))

        return nodes[-1][1] == len(nodes)