class Node:
    # Constructor
    def __init__(self, info, link=None):
        self.info = info
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, info):
        # Create a new node
        newNode = Node(info)
        if self.head != None:
            newNode.link = self.head
            self.head = newNode
        else:
            self.head = newNode
        return self.head

    def display(self):
        current = self.head
        while current != None:
            print(current.info)
            current = current.link

    def reverse_linkedlist(self, prev, curr):
        if curr is None:
            return prev
        # Storing my next
        next_node = curr.link
        # Change my pointers
        curr.link = prev
        # reset
        return self.reverse_linkedlist(curr, next_node)

    def reverse(self):
        self.head = self.reverse_linkedlist(None, self.head)
        return self.head  # Return the head of the reversed linked list


LL = LinkedList()
head = LL.insert_at_beginning(4)
head = LL.insert_at_beginning(3)
head = LL.insert_at_beginning(2)
head = LL.insert_at_beginning(1)

print("Original linked list:")
LL.display()

print("Reversed linked list:")
reversed_head = LL.reverse()
while reversed_head:
    print(reversed_head.info, end=" ")
    reversed_head = reversed_head.link
