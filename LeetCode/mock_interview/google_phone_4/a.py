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
        if not root:
            return []

        delete_vals = set(to_delete)

        forest_que = [root]

        ans = []
        while forest_que:
            # print(forest_que)
            node = forest_que.pop(0)

            if not node:
                continue

            if node.val in delete_vals:
                forest_que.append(node.left)
                forest_que.append(node.right)
                continue

            top = node
            forest = [top]
            while forest:
                node = forest.pop(0)
                if node.left and node.left.val in delete_vals:
                    forest_que.append(node.left)
                    node.left = None
                if node.right and node.right.val in delete_vals:
                    forest_que.append(node.right)
                    node.right = None

                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)

            ans.append(top)

        return ans