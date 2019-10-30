def maxPathSum(tree):
    ans = 0

    def rec(node):
        nonlocal ans
        if node is None:
            return 0
        left = max(0, rec(node.left))
        right = max(0, rec(node.right))
        val = node.value + left + right
        ans = max(ans, val)
        return node.value + max(left, right)

    rec(tree)
    return ans
