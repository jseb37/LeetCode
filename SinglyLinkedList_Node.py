class Node:
    #Constructor
    def __init__(self,info, link = None):
        self.info = info
        self.link = link


#Creating a single node
first = Node(10)
print(first.info)
print(first)