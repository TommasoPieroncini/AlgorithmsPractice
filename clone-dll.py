class Node:
    def __init__(self, data):
        self.next = None
        self.arbit = None
        self.data = data
        self.clone = None

head = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

head.arbit = node2
node1.arbit = node4
node2.arbit = node1
node3.arbit = head
node4.arbit = node2

def makeCopy(head):
    if head == None:
        return None
    myMap = {}
    newHead = Node(head.data)
    newCurr = newHead
    curr = head.next
    #i = 1
    head.clone = newHead
    while curr != None:
        newCurr.next = Node(curr.data)
        newCurr = newCurr.next
        curr.clone = newCurr
        curr = curr.next
    
    curr = head
    while curr != None:
        curr.clone.arbit = curr.arbit.clone
        curr = curr.next
    
    curr = head.next
    while curr != None:
        curr.clone = None
        curr = curr.next
    
    return newHead

newHead = makeCopy(head)

curr = newHead
while curr != None:
    print curr.data, curr.arbit.data
    curr = curr.next