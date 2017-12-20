import math
class Node:
    
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        self.parent = None

node1 = Node(4)
node2 = Node(2)
node3 = Node(6)
node4 = Node(12)
node5 = Node(10)
node6 = Node(3)

node3.left = node1
node1.left = node2
node2.right = node6

node3.right = node4
node4.left = node5

root = node3

def bs(root, data):
    savedNode = bsHelp(root, data, None)
    return savedNode

def bsHelp(node, data, savedNode):
    if node == None:
        return node
    if data == node.data:
        savedNode = node
    elif data > node.data:
        savedNode = bsHelp(node.right, data, savedNode)
    else:
        savedNode = bsHelp(node.left, data, savedNode)
    return savedNode

#print bs(root, 3) == node6


# def bfs(start):
#     visited = set()
#     q = Queue()
#     q.add(start)
#     while len(q) > 0:
#         item = q.pop()
#         if item not in visited:
#             visited.add(item)
#             q.extend(item.neighbors - visited)

# def dfs(start):
#     visited = set()
#     dfsHelp(start, visited)

# def dfsHelp(node, visited):
#     if node not in visited:
#         visited.add(node)
#         for n in node.neighbors - visited:
#             dfsHelp(n, visited)

############################################
#print all permutations of a string
#Get factorial to use for iteration
    #Fix first letter
    #Swap second character with the next one until the end of the string and print each result as a permutation
        #Do this for all letters after the first one
    #Fix a new letter to the first position
    #Repeat
def allPerms(s):
    fact = math.factorial(len(s))
    saved = list(s)
    fixed = 0
    j = 1
    i = 0
    while i < fact:
        k = 0
        listed = list(saved)
        while k < fact/len(s):
            
            while j < len(s) - 1:
                #print new perm
                print "".join(listed)

                #swap
                tmp = listed[j]
                listed[j] = listed[j + 1]
                listed[j + 1] = tmp

                j += 1
                i += 1
                k += 1
            
            j = 1
        fixed += 1
        if fixed == len(s):
            break
        tmp = saved[0]
        saved[0] = saved[fixed]
        saved[fixed] = tmp

#print allPerms("helloyouman?")


######################################################
#Towers of Hanoi
tower1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
tower2 = []
tower3 = []
def moveTop(origin, dest):
    elem = origin.pop()
    dest.append(elem)

def moveDisks(num, origin, dest, buff):
    if num <= 0:
        return

    moveDisks(num - 1, origin, buff, dest)

    moveTop(origin, dest)

    moveDisks(num - 1, buff, dest, origin)

#moveDisks(len(tower1), tower1, tower3, tower2)
#print tower3

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

## Modify string into given length intervals separated by dashes
def kStringIntervals(S, K):
    # write your code in Python 2.7
    myList = list(S)
    n = 0
    for i in range(len(S) - 1, -1, -1):
        if myList[i] == "-":
            del myList[i]
        else:
            n += 1
            if myList[i].isalpha():
                print myList[i]
                myList[i] = myList[i].upper()
                print myList[i]
        if n == K and i > 0:
            myList.insert(i, "-")
            n = 0
    return "".join(myList)

# print solution("2-4A0r7-4k", 4)


#     head = Node(B[0])
#     curr = head
#     for c in B[1:]:
#         node = Node(c)
#         curr.next = node
#         curr = node
#     end = curr
#     end.next = head
    
#     for c in A:


class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# mNode1 = LLNode(-1)
# curr = mNode1
# for i in range(10):
#     print i
#     new = LLNode(i)
#     curr.next = new
#     curr = curr.next
# curr.next = mNode1

## Given a cyclic linked list, remove every other element
def remEvOther(head):
    curr = head
    curr.next = curr.next.next
    curr = curr.next
    while curr != head and curr.next != head:
        curr.next = curr.next.next
        curr = curr.next
    return head


# head = remEvOther(mNode1)
# curr = head
# print curr.data
# curr = curr.next
# while curr != head:
#     print curr.data
#     curr = curr.next

## return longest continuous substring of 2 distinct characters in an input string
# in: aabcaabbab
# out: abbab

def ls2(s):
    if len(s) == 0:
        return ""

    first = s[0]
    second = ""
    res = ""
    longest = ""
    lastIndexOfSecond = 0

    for i in range(len(s)):
        c = s[i]
        if second == "" and c != first:
            second = c
            lastIndexOfSecond = i
        elif c != first and c != second:
            if len(res) > len(longest):
                longest = res
            first = second
            second = c
            res = s[lastIndexOfSecond:i]
            lastIndexOfSecond = i
        elif c != second and c == first and second != "":
            first = second
            second = c
            lastIndexOfSecond = i
        res += c
    if len(res) > len(longest):
        longest = res
    return longest

## print ls2("aabcaabbablkkldiiidddiijdsasasasasasasasasas")


## return a copy of a list of strings with duplicates removed, keep first occurrence
## return a copy of a list of strings with duplicates removed, keep nth occurrence

def copy(l, n):
    result = []
    mMap = {}
    for s in l:
        if s not in mMap:
            mMap[s] = 1
            result.append(s)
        else:
            mMap[s] += 1
            if mMap[s] <= n:
                result.remove(s)
                result.append(s)
    return result

##print copy(["he", "hello", "hello", "h", "he", "hello", "he", "hel"], 2)

# given pointers to two nodes with pointers to their parents in a rooted binary tree (not BST), find out whether they have a common ancestor beside root

def ifAncestor(n1, n2, root):
    if n1 == n2:
        return True
    mSet = set()
    curr = n1
    while curr != root:
        mSet.add(curr)
        curr = curr.parent
    curr = n2
    while curr != root:
        if curr in mSet:
            return True
        curr = curr.parent
    return False

q = Node(1)
r = Node(2)
t = Node(5)
o = Node(12)
qa = Node(1)
ra = Node(2)
ta = Node(5)
oa = Node(12)

q.right = r
q.left = t
r.parent = q
t.parent = q
t.right = o
t.left = qa
o.parent = t
qa.parent = t
qa.left = ra
ra.parent = qa
qa.right = ta
ta.parent = qa
r.right = oa
oa.parent = r

print ifAncestor(qa, t, q)

