# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # find all deepest nodes, bfs
        if root is None:
            return root

        que = [root]
        deepest = set()
        while True:
            children = []
            deepest.clear()
            while que:
                node = que.pop(0)
                deepest.add(node.val)
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            if len(children) == 0:
                break
            que = children

        # find subtree node which has all deepest nodes as children
        def dfs(node):
            if not node or node.val in deepest:
                return node
            l = dfs(node.left)
            r = dfs(node.right)
            return node if l and r else l or r

        return dfs(root)
