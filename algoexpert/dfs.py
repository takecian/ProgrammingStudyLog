# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        stack = [self]
        while stack:
            node = stack.pop()
            array.append(node.name)
            for child in reversed(node.children):
                stack.append(child)
        return array


