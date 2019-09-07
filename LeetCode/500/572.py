class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def find_start_nodes(node, target):
            ans = []
            if not node:
                return ans
            if node.val == target.val:
                ans.append(node)
            left = find_start_nodes(node.left, target)
            ans += left
            right = find_start_nodes(node.right, target)
            ans += right
            return ans

        s_roots = find_start_nodes(s, t)
        if len(s_roots) == 0:
            return False

        def is_same(one, two):
            if one is None and two is None:
                return True
            if one is None or two is None:
                return False

            if one.val != two.val:
                return False

            return is_same(one.left, two.left) and is_same(one.right, two.right)

        for s_root in s_roots:
            if is_same(s_root, t):
                return True
        return False