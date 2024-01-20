class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right= None
class BST:
    def buildBst(self,root,ele):
        if root == None:
            return Node(ele)
        elif ele<root.data:
            root.left=self.buildBst(root.left,ele)
        elif ele>root.data:
            root.right=self.buildBst(root.right,ele)
        return root

root = None
b = BST()
for ele in [10,5,25,2,7,30]:
    root = b.buildBst(root,ele)