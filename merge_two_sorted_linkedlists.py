'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
'''

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


def mergeTwoLists(l1,l2):
    dummy = Node(0)
    current = dummy
    while l1 and l2:
        if l1.info < l2.info:
            current.link = l1
            l1 = l1.link
        else:
            current.link = l2
            l2 = l2.link
        current = current.link
        # Attach remaining elements of l1 or l2
        if l1:
            current.link = l1
        else:
            current.link = l2

    return dummy.link


list1 = LinkedList()

list1.insert_at_beginning(4)
list1.insert_at_beginning(2)
list1.insert_at_beginning(1)
list1.display()

list2 = LinkedList()

list2.insert_at_beginning(4)
list2.insert_at_beginning(3)
list2.insert_at_beginning(1)
list2.display()

merged_list = mergeTwoLists(list1.head, list2.head)
# Print the merged list
while merged_list:
    print(merged_list.info, end=" -> ")
    merged_list = merged_list.link
print("None")


