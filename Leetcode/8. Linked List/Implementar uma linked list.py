class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self):
        new_node = Node()
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node

        else:
            self.tail = new_node

        self.head = new_node


    def add_to_tail(self):
        new_node = Node()
        new_node.next = self.tail

        if self.tail:
            self.tail.next = new_node

        else:
            self.head = new_node

        self.tail = new_node


    def remove_from_head(self):
        if not self.head:
            return None

        removed_node = self.head.value

        self.head = self.head.prev

        if self.head:
            self.head.prev = None

        else:
            self.head = None

        return removed_node

    def remove_from_tail(self):
        if not self.tail:
            return None

        removed_node = self.tail.prev

        self.tail = self.tail.next

        if self.tail:
            self.tail.next = None

        else:
            self.tail = None

        return removed_node