class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
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
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    def search(self, data):
        return self.__search_recursive(self.root, data)

    def __search_recursive(self, node, data):
        if node is None:
            return False

        if node.data == data:
            return True
        elif data <  node.data:
            return self.__search_recursive(node.left, data)
        else:
            return self.__search_recursive(node.right, data)


tree = BinaryTree()

tree.insert(5)
tree.insert(3)
tree.insert(2)
tree.insert(4)
tree.insert(1)
tree.insert(7)

print(tree.search(3))
print(tree.search(2))
print(tree.search(6))
print(tree.search(8))
print(tree.search(9))