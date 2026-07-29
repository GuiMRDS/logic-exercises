from unittest import result


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left:
                self._insert_recursive(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._insert_recursive(node.right, val)
            else:
                node.right = TreeNode(val)

    def inoder_traversal(self):
        result = []
        self._inoder_traversal(self.root, result)
        return result

    def _inoder_traversal(self, node, result):
        if node:
            self._inoder_traversal(node.left, result)
            result.append(node.val)
            self._inoder_traversal(node.right, result)


tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(1)
tree.insert(10)
tree.insert(15)
tree.insert(7)


print("inoder traversal: ", tree.inoder_traversal())