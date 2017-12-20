class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findCycles(s):
    if s == None or s == "":
        return False, "invalid string"

    head = Node(s[0])

    curr = head

    for c in s[1:]:
        if curr.next == None:
            if curr.data != c and head.data == c:
                curr.next = head
                curr = head
            else:
                new = Node(c)
                curr.next = new
                curr = new
        elif curr.next.data == c:
            curr = curr.next
        else:
            new = Node(c)
            new.next = curr.next
            curr.next = new
            curr = new
    
    if curr.next == None:
        return False, "no cycle"
    
    curr = curr.next
    start = curr
    cycle = ""
    for c in s:
        if curr == start:
            cycle = ""
        if curr.data != c or curr.next == None:
            return False, "no cycle"
        cycle += curr.data
        curr = curr.next
    
    return True, cycle

print findCycles("ferferferfertferferferfert")