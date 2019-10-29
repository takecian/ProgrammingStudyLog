def findClosestValueInBst(tree, target):
    # Write your code here.
    ptr = tree
    ans = 0
    min_diff = 10 ** 10

    while True:
        diff = abs(tree.value - target)
        if diff < min_diff:
            ans = tree.value
            min_diff = diff
        if tree.value < target:
            if tree.right:
                tree = tree.right
            else:
                break
        else:
            if tree.left:
                tree = tree.left
            else:
                break

    return ans

