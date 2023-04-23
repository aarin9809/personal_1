class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy

    def insert(self,data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

    def delete(self):
        pop_data = 