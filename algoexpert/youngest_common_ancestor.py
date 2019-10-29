def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    def calc_height(node):
        height = 0
        while node != topAncestor:
            height += 1
            node = node.ancestor
        return height

    height_one = calc_height(descendantOne)
    height_two = calc_height(descendantTwo)

    node_one = descendantOne
    node_two = descendantTwo
    diff = abs(height_one - height_two)
    if height_one > height_two:
        while diff > 0:
            diff -= 1
            node_one = node_one.ancestor
    else:
        while diff > 0:
            diff -= 1
            node_two = node_two.ancestor
    while node_one != node_two:
        node_one = node_one.ancestor
        node_two = node_two.ancestor

    return node_one