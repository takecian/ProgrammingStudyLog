# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        que = [root]
        while que:
            if len(ans) % 2 == 0:
                ans.append([node.val for node in que])
            else:
                ans.append([node.val for node in reversed(que)])

            next_que = []
            while que:
                node = que.pop(0)
                if node.left:
                    next_que.append(node.left)
                if node.right:
                    next_que.append(node.right)

            que = next_que

        return ans
