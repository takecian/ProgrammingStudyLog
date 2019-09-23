class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans

        que = [root]
        ans.append(root.val)
        while True:
            next_que = []
            while que:
                node = que.pop(0)
                if node.left:
                    next_que.append(node.left)
                if node.right:
                    next_que.append(node.right)
            que = next_que
            if not que:
                break
            ans.append(que[-1].val)
        return ans