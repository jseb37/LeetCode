'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Input: root = [3,9,20,null,null,15,7]
Output: 3
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right= None
class BST:
    def buildBst(self,root,ele):
        if root == None:
            return Node(ele)
        if ele<root.data:
            root.left=self.buildBst(root.left,ele)
        else:
            root.right=self.buildBst(root.right,ele)
        return root
def maxdepth(root):
    if not root:
        return 0
    return 1 + max(maxdepth(root.left),maxdepth(root.right))


root = None
b = BST()
for ele in [10,5,25,2,7,30]:
    root = b.buildBst(root,ele)

print(maxdepth(root))