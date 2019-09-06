class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        left_num = 0
        right_num = 0

        def countChild(node):
            nonlocal left_num
            nonlocal right_num
            if node is None:
                return 0
            l = countChild(node.left)
            r = countChild(node.right)
            if node.val == x:
                left_num = l
                right_num = r
            return 1 + l + r

        countChild(root)
        rest = n - left_num - right_num - 1

        blue_count = max(left_num, right_num, rest)
        red_count = sum([left_num, right_num, rest]) - max(left_num, right_num, rest) + 1
        return blue_count > red_count

