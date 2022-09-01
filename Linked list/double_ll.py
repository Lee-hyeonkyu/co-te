class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Double_Linked_list:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == "":
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def show_node(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_head(self, data):
        if self.head == "":
            return False
        node = self.head
        while node:
            if node.data == data:
                return node.data
            else:
                node = node.next
        return False

    def search_tail(self, data):
        if self.head == "":
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node.data
            else:
                node = node.prev
        return False

    def pre_insert(self, data, pre_data):
        if self.head == "":
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != pre_data:
                node = node.prev
                if node == "":
                    return False
            new = Node(data)
            pre_new = node.prev
            pre_new.next = new
            new.prev = pre_data
            new.next = node
            node.prev = new
            return True


a = Double_Linked_list(0)

for i in range(1, 11):
    a.insert(i)

# a.show_node()
# print(a.search_head(3))
# print(a.search_tail(5))
a.pre_insert(1.5, 2)

a.show_node()
