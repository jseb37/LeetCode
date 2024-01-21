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
    def search(self,root,ele):
        if root==None or root.data==ele:
            return root
        elif ele<root.data:
           return self.search(root.left,ele)
        elif ele>root.data:
            return self.search(root.right,ele)
    def minimum(self,root):
        if root.left == None:
           return root.data
        return self.minimum(root.left)
    def maximum(self,root):
       if root.right == None:
          return root.data
       return self.maximum(root.right)
root = None
b = BST()
for ele in [10,5,25,2,7,30]:
    root = b.buildBst(root,ele)
m=b.minimum(root)
print("Min value is {}".format(m))
ma=b.maximum(root)
print("Max value is {}".format(ma))
s=b.search(root,30)
if s == None:
   print("Element Not Found")
elif s != None:
   print("Found {}".format(s.data))