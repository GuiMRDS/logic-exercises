class TreeNode:
    def  __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(5)


def postorder(node):
    if not node:
        return
    postorder(node.left) # Abir esquerda
    print(node.val, end=" ") # Abrir esquerda
    postorder(node.right) # Abrir direita


postorder(root)