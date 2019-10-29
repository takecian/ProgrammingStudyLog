def invertBinaryTree(tree):
    # Write your code here.
    def invert(node):
        if node is None:
            return
        node.left, node.right = node.right, node.left
        invert(node.left)
        invert(node.right)

    invert(tree)
    return tree
