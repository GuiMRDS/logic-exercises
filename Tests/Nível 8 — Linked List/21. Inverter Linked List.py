# 1 → 2 → 3 → 4 → 5

# 5 → 4 → 3 → 2 → 1

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
        if not self.head:
            self.head = new_node
        else:
