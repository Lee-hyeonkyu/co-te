class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linked_List:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == "":
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def show_node(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == "":
            return

        if self.head.data == data:
            tmp = self.head
            self.head = self.head.next
            del tmp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    tmp = node.next
                    node.next = node.next.next
                    del tmp
                else:
                    node = node.next

    def search_node(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node.data
            else:
                node = node.next
        return False

# def search_node(self,data):
#     node = self.head
#     while node:
#         if node.data == data:
#             return node.data
#         elif node.next != "":
#             node = node.next


a = Linked_List(0)

for i in range(1, 11):
    a.add(i)


# a.delete(5)


print(a.show_node())
# print(a.search_node(8))
