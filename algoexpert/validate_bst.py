def validateBst(tree):
    # Write your code here.
    return validate(tree, -10 ** 10, 10 ** 10)


def validate(tree, min_value, max_value):
    if tree is None:
        return True
    if tree.value < min_value or max_value <= tree.value:
        return False

    return validate(tree.left, min_value, tree.value) and validate(tree.right, tree.value, max_value)
