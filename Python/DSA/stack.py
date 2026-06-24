class Stack:
    def __init__(self, max_lenght = 1000):
        self.items = [0] * max_lenght
        self.max_lenght = max_lenght
        self.pointer = 0

    def push(self, item):
        self.items[self.pointer] = item
        self.pointer += 1

    def pop(self):
        if not len(self.items):
            raise IndexError('pop from an empty stack')

        return self.items.pop()

    def peek(self):
        if not len(self.items):
            raise IndexError('pop from an empty stack')

        return self.items[-1]

    def size(self):
        return len(self.items)