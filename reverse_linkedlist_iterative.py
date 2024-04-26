class Node:
    #Constructor
    def __init__(self,info,link = None):
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

    def reverse_linkedlist(self):
        prev = None
        curr = self.head
        while curr!=None:
            #Storing my next
            next_node = curr.link
            #Change my pointers
            curr.link = prev
            #reset
            prev = curr
            curr = next_node
        return prev

LL = LinkedList()
LL.insert_at_beginning(4)
LL.insert_at_beginning(3)
LL.insert_at_beginning(2)
LL.insert_at_beginning(1)
LL.display()
print("********")
reversed_head = LL.reverse_linkedlist()
print(reversed_head)
while reversed_head:
    print(reversed_head.info, end=" ")
    reversed_head = reversed_head.link
