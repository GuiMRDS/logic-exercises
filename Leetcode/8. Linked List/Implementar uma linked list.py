# 1 → 2 → 3 → 4 → 5
# 5 → 4 → 3 → 2 → 1


class Node:
    def __init__(self, next, prev):
        self.next = next
        self.prev = prev


class linkedList:
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
        new_node.next = self.tail

        if self.tail:
            self.tail.prev = new_node
        else:
            self.head = new_node

        self.tail = new_node


    def remove_from_head(self, value):
        if not self.head:
            return None

        removed_node = self.head.value

        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.head = None

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