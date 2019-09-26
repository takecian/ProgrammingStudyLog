class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        prev_que = []
        que = [(root, 0)]
        level = 0
        while True:
            next_que = []
            prev_que = []
            while que:
                node, index = que.pop(0)
                prev_que.append((node, index))
                if node.left:
                    next_que.append((node.left, index * 2 + 1))
                if node.right:
                    next_que.append((node.right, index * 2 + 2))
            level += 1
            que = next_que

            if len(prev_que) != 2 ** (level - 1):
                if len(que) > 0:
                    return False
            if len(que) == 0:
                que = prev_que
                break

        index = 2 ** (level - 1) - 1
        # print(que, index)
        while que:
            node, i = que.pop(0)
            if index != i:
                return False
            index += 1
        return True