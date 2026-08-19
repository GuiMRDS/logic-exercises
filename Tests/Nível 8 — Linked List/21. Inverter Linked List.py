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


    def remove_from_head(self, value):
        if not self.head:
            return None

        removed_node = self.head.value

        self.head = self.head.next
        if self.head:
            self.head.prev = None
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


linked_list = LinkedList()

linked_list.add_to_head(10)
linked_list.add_to_head(20)
linked_list.add_to_head(30)
linked_list.add_to_head(40)
linked_list.add_to_head(50)
linked_list.add_to_tail(60)
linked_list.add_to_tail(70)
linked_list.add_to_tail(80)
linked_list.add_to_tail(90)
linked_list.add_to_tail(100)

linked_list.remove_from_head(20)
linked_list.remove_from_head(10)
linked_list.remove_from_head(20)

linked_list.remove_from_tail(100)

print(linked_list.head.value)
print(linked_list.head.next.value)
print(linked_list.head.next.next.value)
print(linked_list.head.next.next.next.value)
print(linked_list.head.next.next.next.value)
print(linked_list.head.next.next.next.next.value)

print(linked_list.tail.value)
print(linked_list.tail.prev.value)
print(linked_list.tail.prev.prev.value)
print(linked_list.tail.prev.prev.prev.value)
print(linked_list.tail.prev.prev.prev.prev.value)


