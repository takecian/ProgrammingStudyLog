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
        def get_leaf(node):
            if node.left is None and node.right is None:
                return set([node.val])
            leafs = []
            if node.left:
                leafs += get_leaf(node.left)
            if node.right:
                leafs += get_leaf(node.right)
            return set(leafs)

        def dfs(node):
            if node.left is None and node.right is None:
                if get_leaf(node) >= deepest:
                    return node
                else:
                    return None
            if node.left:
                ret = dfs(node.left)
                if ret:
                    return ret
            if node.right:
                ret = dfs(node.right)
                if ret:
                    return ret

            if get_leaf(node) >= deepest:
                return node
            else:
                return None

        return dfs(root)