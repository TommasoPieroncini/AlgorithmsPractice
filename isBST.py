class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

n1 = Node(5, None, None)
n5 = Node(10, None, None)
n4 = Node(16, n5, None)
n3 = Node(3, None, None)
n2 = Node(4, n3, n1)
root = Node(6, n2, n4)

def isBST(root):
    if root is None:
        return False
    isBST = help(root, None, False, True)
    return isBST

def help(root, prevData, isLeft, isBST):
    if not isBST:
        return False
    if prevData is not None:
        if isLeft:
            if root.data > prevData:
                return False
    if root.left is not None:
        isBST = help(root.left, root.data, True, isBST)
    if root.right is not None:
        isBST = help(root.right, root.data, False, isBST)
    
    return isBST

print isBST(root)