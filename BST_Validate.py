
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

    def helper(self, root, left, right):
        if root is None:
            return True
        if not (left < root.data < right):
            return False
        return self.helper(root.left, left, root.data) and self.helper(root.right, root.data, right)

    def isValidBST(self, root):
        return self.helper(root, float('-inf'), float('inf'))

root = None
listA=[]
b = BST()
for ele in [10,5,25,2,7,30]:
    root = b.buildBst(root,ele)

a=b.isValidBST(root)
if a:
    print("valid bst")
else:
    print("invalid bst")