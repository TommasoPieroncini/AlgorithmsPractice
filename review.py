from Queue import *
class BTNode:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data



node0 = BTNode(559)
node1 = BTNode(270)
node2 = BTNode(142)
node3 = BTNode(69)
node2.left = node3
node1.left = node2
node4 = BTNode(460)
node5 = BTNode(360)
node4.left = node5
node1.right = node4
node0.left = node1
node6 = BTNode(836)
node7 = BTNode(770)
node8 = BTNode(647)
node7.left = node8
node6.left = node7
node9 = BTNode(923)
node6.right = node9
node0.right = node6
# 
# 
# This is the root of a binary search tree with 10 nodes.
treeRootnode0 = node0

def onData(data):
    print data

def bfs(root, func):
    queue = Queue()
    queue.put(root)

    while not queue.empty():
        node = queue.get()
        func(node.data)
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)

print "BFS traversal"
bfs(treeRootnode0, onData)

def dfs(root, func):
    stack = []
    stack.append(root)

    while len(stack) != 0:
        node = stack.pop()
        func(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
print "\nDFS traversal"
dfs(treeRootnode0, onData)
