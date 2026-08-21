# 1 → 2 → 3 → 4
#          ↑   ↓
#           ← ←


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

        if self.head == None:
            self.head.prev = new_node

        else:
            self.tail.next = new_node

        self.head = new_node


    def add_to_tail(self, value):
        new_node = Node(value)
        new_node.prev = self.tail

        if self.tail == None:
            self.tail.next = new_node

        else:
            self.head.prev = new_node

        self.tail = new_node


    def remove_from_head(self):
        if not self.tail:
            return None

        removed_node = self.tail

        self.tail = self.tail.next
        if self.tail:
            self.tail.prev = None

        else:
            self.tail = None

        return removed_node

    def remove_from_tail(self, value):
        if not self.tail:
            return None

        removed_node = self.tail.value

        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        return removed_node


