class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if root is None:
            return ans

        que = [root]
        while True:
            next_que = []
            same_level_node_values = []
            while que:
                node = que.pop(0)
                same_level_node_values.append(node.val)

                if node.left:
                    next_que.append(node.left)

                if node.right:
                    next_que.append(node.right)

            ans.append(same_level_node_values)
            que = next_que
            if not que:
                break
        return ans