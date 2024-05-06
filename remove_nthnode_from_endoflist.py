'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''
class Node:
    #Constructor
    def __init__(self,info, link = None):
        self.info = info
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,info):
       #Create a new node
       newNode = Node(info)
       if self.head != None:
           newNode.link = self.head
           self.head = newNode
       else:
           self.head = newNode

    def display(self):
        current = self.head
        while current != None:
            print(current.info)
            current = current.link

def removeNthFromEnd(head,n):
    dummy=Node(0,head)
    left=dummy
    right=head

    while n > 0 and right:
        right = right.link
        n-=1

    while right:
        left=left.link
        right=right.link
    #Delete
    left.link = left.link.link
    return dummy.link



LL = LinkedList()
LL.insert_at_beginning(9)
LL.insert_at_beginning(7)
LL.insert_at_beginning(6)
LL.insert_at_beginning(4)
LL.insert_at_beginning(5)
LL.display()
print("*****")
node=removeNthFromEnd(LL.head,2)
while node:
    print(node.info,end =" ")
    node=node.link