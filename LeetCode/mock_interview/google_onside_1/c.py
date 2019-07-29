# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        if root is None:
            return []

        delete_targets = set(to_delete)

        ans = []
        que = [root]

        while que:
            head = que.pop(0)
            if head is None:
                continue
            if head.val in delete_targets:
                que.append(head.left)
                que.append(head.right)
                continue

            ans.append(head)

            sub_que = [head]  # BFS
            while sub_que:
                node = sub_que.pop(0)

                if node is None:
                    continue

                if node.left and node.left.val in delete_targets:
                    delete_node = node.left
                    que.append(delete_node.left)
                    que.append(delete_node.right)
                    node.left = None
                else:
                    sub_que.append(node.left)

                if node.right and node.right.val in delete_targets:
                    delete_node = node.right
                    que.append(delete_node.left)
                    que.append(delete_node.right)
                    node.right = None
                else:
                    sub_que.append(node.right)

        return ans