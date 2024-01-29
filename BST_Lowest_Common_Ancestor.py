#Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
#According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

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

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        cur = root
        while cur:
            if p.data<cur.data and q.data<cur.data:
                cur=cur.left
            elif p.data>cur.data and q.data>cur.data:
                cur=cur.right
            else:
                return cur
root = None
b = BST()
for ele in [6,2,8,0,4,7,9,3,5]:
    root = b.buildBst(root, ele)

l=b.lowestCommonAncestor(root,Node(2),Node(8))
print(l.data)