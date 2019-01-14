class BTNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

#         0
#       /   \
#      1     6
#     / \   / \
#    2   4 7   9
#   /   / /
#  3   5 8

node0 = BTNode(508)
node1 = BTNode(296)
node2 = BTNode(151)
node3 = BTNode(11)
node2.left = node3
node1.left = node2
node4 = BTNode(470)
node5 = BTNode(308)
node4.left = node5
node1.right = node4
node0.left = node1
node6 = BTNode(890)
node7 = BTNode(744)
node8 = BTNode(668)
node7.left = node8
node6.left = node7
node9 = BTNode(970)
node6.right = node9
node0.right = node6
# 
# 
# This is the root of a binary search tree with 10 nodes.
treeRootnode0 = node0


preorder = [3, node0, node1, node2, node3, node4, node5, node6, node7, node8, node9]


def findOuterNodes(preorder):
    outerNodes = my_dfs(preorder[1], True, preorder[1], [], preorder[0])
    for n in outerNodes:
        print(n.data)

def my_dfs(root, is_root, orig_root, outerNodes, currHeight):
    if root.left != None:
        if is_root:
            outerNodes.append(root)
        outerNodes = my_dfs(root.left, is_root, orig_root, outerNodes, currHeight - 1)
    is_root = False
    if root == orig_root:
        orig_root = root.right
        if root not in outerNodes:
          outerNodes.append(root)
    if root.right != None:
        outerNodes = my_dfs(root.right, is_root, orig_root, outerNodes, currHeight - 1)
    if root.left == None and root.right == None and currHeight == 0:
        outerNodes.append(root)
    return outerNodes

findOuterNodes(preorder)