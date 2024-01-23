#Postorder Traversal - LeftNode,RightNode,RootNode
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

    def preorder(self,root):
        if root == None:
            return
        self.preorder(root.left)
        self.preorder(root.right)
        print(root.data)

root = None
b = BST()
for ele in [10,5,25,2,7,30]:
    root = b.buildBst(root,ele)
b.preorder(root)
