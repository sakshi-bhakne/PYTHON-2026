# first Create a node:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#create a class that manges nodes:
class LinkedList:
    def __init__(self):
        self.head = None
#insert nodes into list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


mylist = LinkedList()

mylist.insert_end(10)
mylist.insert_end(20)
mylist.insert_end(30)

mylist.display()
