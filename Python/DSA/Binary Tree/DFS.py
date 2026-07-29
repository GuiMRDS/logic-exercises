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

    def dfs(self, val):
        return self._dfs_recursive(self.root, val)

    def _dfs_recursive(self, node, val):
        if node:
            print(node.val)
        if not node:
            return False
        if node.val == val:
            return True

        if self._dfs_recursive(node.left, val):
            return True

        if self._dfs_recursive(node.right, val):
            return True


tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(1)
tree.insert(10)
tree.insert(15)
tree.insert(7)
tree.insert(20)


print("Depth First Search - profundidade: ", tree.dfs(20))