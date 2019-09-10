from collections import defaultdict

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        node_list = defaultdict(list)
        def traverse(node, level):
            if node is None:
                return
            que = [(node, level)]
            while que:
                n, l = que.pop(0)
                if n:
                    node_list[l].append(n.val)
                    que.append((n.left, l-1))
                    que.append((n.right, l+1))

        traverse(root, 0)
        return [node_list[i] for i in sorted(node_list.keys())]
