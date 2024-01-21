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
    def mini(self,root):
        if root.left == None:
           return root.data
        return self.mini(root.left)
    def maxim(self,root):
       if root.right == None:
          return root.data
       return self.maxim(root.right)
root = None
b = BST()
for ele in [10,5,25,2,7,30]:
    root = b.buildBst(root,ele)
m=b.mini(root)
print("Min value is {}".format(m))
ma=b.maxim(root)
print("Max value is {}".format(ma))