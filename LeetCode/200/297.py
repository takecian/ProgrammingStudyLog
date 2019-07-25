# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def dfs(node):
            if node is None:
                val.append(-10 * 10)
                return
            val.append(node.val)
            dfs(node.left)
            dfs(node.right)

        val = []
        dfs(root)
        # print(str(val))
        return str(val)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs():
            if len(src) == 0:
                return None
            val = src.pop(0)
            if val != -10 * 10:
                node = TreeNode(val)
            else:
                return None

            node.left = dfs()
            node.right = dfs()
            return node

        src = list(map(int, data[1:-1].split(',')))
        root = dfs()
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))