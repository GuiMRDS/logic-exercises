# 1 → 2 → 3 → 4 → 5

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node

        else:
            self.tail = new_node

        self.head = new_node


    def add_to_tail(self, value):
        new_node = Node(value)
        new_node.prev = self.tail

        if self.tail:
            self.tail.next = new_node

        else:
            self.head = new_node

        self.tail = new_node


    def remove_from_head(self):
        if not self.head:
            return False

        removed_node = self.head.next

        self.head = self.head.next

        if self.head:
            self.head.prev = None
        else:
            self.tail = None


        return removed_node


    def remove_from_tail(self):
        if not self.tail:
            return False

        removed_node = self.tail.prev

        self.tail = self.tail.prev

        if self.tail:
            self.tail.next = None
        else:
            self.tail = None


        return removed_node



linked_list = LinkedList()
linked_list.add_to_head(1)
linked_list.add_to_head(2)
linked_list.add_to_head(3)
linked_list.add_to_tail(4)
linked_list.add_to_tail(5)