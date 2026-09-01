# 1 → 2 → 3 → 4 → 5
# 5 → 4 → 3 → 2 → 1


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, prev, next):
        self.head = prev
        self.tail = next


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
            self.tail = new_node

        self.tail = new_node


    def remove_from_head(self):
        if not self.head:
            return None

        removed_node = self.head.value

        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        return removed_node

    def remove_from_tail(self):
        if not self.tail:
            return None

        removed_node = self.tail.value

        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        return removed_node




linked_list = LinkedList(None, None)

add_to_head = linked_list.add_to_head(1)
add_to_head = linked_list.add_to_head(2)
add_to_head = linked_list.add_to_head(3)
add_to_tail = linked_list.add_to_tail(4)
add_to_tail = linked_list.add_to_tail(5)
