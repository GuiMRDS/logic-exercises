class  Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.data, node.right)


    def search(self, data):
        return self.__seacrch_recursive(self.root, data)

    def __seacrch_recursive(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self.__seacrch_recursive(node.left, data)
        else:
            return self.__seacrch_recursive(node.right, data)


tree = BinaryTree()
tree.insert(6)
tree.insert(2)
tree.insert(4)
tree.insert(7)
tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(5)
tree.insert(9)

print("Search 4:", tree.search(4))
print("Search 6:", tree.search(6))