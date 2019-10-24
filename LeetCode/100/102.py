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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        que = [root]

        while que:
            ans.append([node.val for node in que])
            next_que = []

            while que:
                node = que.pop(0)
                if node.left:
                    next_que.append(node.left)
                if node.right:
                    next_que.append(node.right)

            que = next_que

        return ans


