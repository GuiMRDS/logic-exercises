# 1 → 2 → 3 → 4 → 5

# Saída:
# 3

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
