class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def find(node):
            if not node:
                return None
            if node.val == p.val or node.val == q.val:
                return node
            left_ans = find(node.left)
            right_ans = find(node.right)
            if left_ans and right_ans:
                return node
            if left_ans is not None:
                return left_ans
            if right_ans is not None:
                return right_ans
            return None

        return find(root)

