from requests import head


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data, next = None):
        self.head = Node(data)
        self.next = next

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

node1 = Node(2)


print(node1.data)