'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 Input: head = [1,2,3,4]
Output: [1,4,2,3]
'''
from collections import deque
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

def reorderlist(l1):
    if not l1:
        return
    q = deque()
    node = l1
    while True:
        node = node.link
        if not node:
            break
        q.append(node)
    while q:
        if l1:
            temp = q.pop()
            l1.link = temp
            l1 = l1.link
        if l1 and q:
            temp = q.popleft()
            l1.link = temp
            l1 = l1.link

    l1.link = None
    return l1


LL = LinkedList()
LL.insert_at_beginning(4)
LL.insert_at_beginning(3)
LL.insert_at_beginning(2)
LL.insert_at_beginning(1)
#LL.display()
list1=reorderlist(LL.head)
while list1:
    print(list1.info)
    list1 = list1.link
