from collections import deque


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        big_int = 10 ** 10
        ans = 1
        que = deque()
        que.append((root, 0))
        levels = []
        while True:
            while que:
                node, index = que.popleft()
                if node.left:
                    levels.append((node.left, index * 2 + 1))

                if node.right:
                    levels.append((node.right, index * 2 + 2))

            if len(levels) == 0:
                break

            width = levels[-1][1] - levels[0][1] + 1
            ans = max(ans, width)

            for l in levels:
                que.append(l)
            levels = []
        return ans