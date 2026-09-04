class Stack:
    def __init__(self):
        self.items = []


    def push(self, item):
        self.items.append(item)


    def pop(self):
        if not len(self.items):
            raise IndexError("Empty list")

        return self.items.pop()


    def peek(self):
        if not len(self.items):
            raise IndexError("Empty list")

        return self.items[-1]


    def size(self):
        return len(self.items)



class StackPointer:
    def __init__(self, max_length=1000):
        self.items = [0] * max_length
        self.max_length = max_length
        self.pointer = 0


    def push(self, item):
        if self.pointer >= self.max_length:
            raise IndexError("Stack overflow")

        self.items[self.pointer] = item
        self.pointer += 1


    def pop(self):
        if self.pointer == 0:
            raise IndexError("Emply Stack")

        self.pointer -= 1
        return self.items[self.pointer]


    def peek(self):
        if self.pointer == 0:
            raise IndexError("Emply Stack")

        return self.items[self.pointer - 1]

    def size(self):
        return self.pointer