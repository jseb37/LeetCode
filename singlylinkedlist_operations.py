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

LL = LinkedList()
LL.insert_at_beginning(10)


