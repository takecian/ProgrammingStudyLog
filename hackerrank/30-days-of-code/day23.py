import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        ans = []
        queue = []
        if root == Node:
            return
        queue.append(root)
        while queue:
            n = queue.pop(0)
            ans.append(str(n.data))
            if n.left != None:
                queue.append(n.left)
            if n.right != None:
                queue.append(n.right)

        print(' '.join(ans))

T=int(input())