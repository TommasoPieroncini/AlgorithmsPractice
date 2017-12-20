import sys
perTable = ["Ac","Ag","Al","Am","Ar","As","At","Au","B","Ba","Be","Bh","Bi","Bk","Br","C","Ca","Cd","Ce","Cf","Cl","Cm","Cn","Co","Cr","Cs","Cu","Db","Ds","Dy",
"Er",
"Es",
"Eu",
"F",
"Fe",
"Fl",
"Fm",
"Fr",
"Ga",
"Gd",
"Ge",
"H",
"He",
"Hf",
"Hg",
"Ho",
"Hs",
"I",
"In",
"Ir",
"K",
"Kr",
"La",
"Li",
"Lr",
"Lu",
"Lv",
"Md",
"Mg",
"Mn",
"Mo",
"Mt",
"N",
"Na",
"Nb",
"Nd",
"Ne",
"Ni",
"No",
"Np",
"O",
"Os",
"P",
"Pa",
"Pb",
"Pd",
"Pm",
"Po",
"Pr",
"Pt",
"Pu",
"Ra",
"Rb",
"Re",
"Rf",
"Rg",
"Rh",
"Rn",
"Ru",
"S",
"Sb",
"Sc",
"Se",
"Sg",
"Si",
"Sm",
"Sn",
"Sr",
"Ta",
"Tb",
"Tc",
"Te",
"Th",
"Ti",
"Tl",
"Tm",
"U",
"Uuo",
"Uup",
"Uus",
"Uut",
"V",
"W",
"Xe",
"Y",
"Yb","Zn","Zr"]
def canMakeWord(w):
    if w == "":
        return False
    state = [False for i in range(len(w) + 1)]
    state[0] = True
    for i in range(1, len(w) + 1):
        ss = w[i - 1]
        x = i - 1
        while not state[i]:
            if state[x]:
                for el in perTable:
                    state[i] = (el == ss)
                    if state[i]:
                        break
            if x == 0:
                break
            x -= 1
            ss = w[x:i]
            if i-x > 3:
                break
    return state[len(state) - 1]

# print canMakeWord("")
numbers = [-3, 4, -1, -2, 9]
def cntgsSum(numbers):

    if len(numbers) == 0:
        return None
    
    largest = numbers[0]
    curr = numbers[0]

    for n in numbers[1:]:
        curr = max(n, curr + n)
        largest = max(curr, largest)
    return largest

# print cntgsSum(numbers)



class Node:
    
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        self.parent = None
        self.next = None

A = Node(65)
B = Node(40)
C = Node(32)
D = Node(25)
E = Node(85)
F = Node(79)
G = Node(87)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G


# Two of the nodes of a BST are swapped. Correct the BST

def correctBst(root):

    bad1 = modPreOrder(root, None, -sys.maxint, sys.maxint)
    
    modBS(root, bad1, -sys.maxint, sys.maxint)

    return root

def modPreOrder(curr, bad1, mmin, mmax):
    if curr == None:
        return bad1
    if bad1 != None:
        return bad1
    if curr.data < mmin or curr.data > mmax:
        return curr
    bad1 = modPreOrder(curr.left, bad1, mmin, curr.data)
    if bad1 != None:
        return bad1
    bad1 = modPreOrder(curr.right, bad1, curr.data, mmax)
    return bad1

def modBS(curr, bad1, mmin, mmax):
    if curr == None:
        return
    if curr.data < mmin or curr.data > mmax:
        tmp = curr.data
        curr.data = bad1.data
        bad1.data = tmp
        return
    if bad1.data < curr.data:
        modBS(curr.left, bad1, mmin, curr.data)
    elif bad1.data > curr.data:
        modBS(curr.right, bad1, curr.data, mmax)
    

# def modBs(node, first, parent, mmin, mmax, prev):
        

#print correctBst(A).data
# A = correctBst(A)

# print A.data, A.left.data, A.right.data, B.left.data, B.right.data, C.left.data, C.right.data

    

# 10, 78, 45
            
#          50
#        /    \
#       35     78
#      / \     / \
#     63  45  10  89

# Reverse a linked list in O(n) and O(1) space

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)
i = Node(9)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = i

def reverseLL(root):
    
    tail, root = helpRevLL(root, None)
    return root

def helpRevLL(curr, root):
    if curr == None:
        return curr, root
    if curr.next != None:
        prev, root = helpRevLL(curr.next, root)
        prev.next = curr
    else:
        root = curr
    return curr, root

# print reverseLL(a).data
# print i.data, i.next.data, h.next.data, g.next.data, f.next.data, e.next.data, d.next.data, c.next.data, b.next.data

q = Node(1)
w = Node(2)
e = Node(3)
r = Node(4)
t = Node(5)
y = Node(6)
u = Node(7)
i = Node(8)
o = Node(9)
p = Node(10)

q.next = w
w.next = e
e.next = r
r.next = t
t.next = y
y.next = u
u.next = i
i.next = o
o.next = p
p.next = t

def detectCycleLL(root):
    currI = root
    currK = root

    while True:
        if currI.next == None or currK.next == None or currK.next.next == None:
            return False
        currI = currI.next
        currK = currK.next.next
        if currI == currK:
            break
    
    currI = root

    while currI != currK:
        currI = currI.next
        currK = currK.next
    
    return currI

#print detectCycleLL(q).data

aq = Node(6)
sw = Node(6)
de = Node(6)
fr = Node(6)
gt = Node(6)
hy = Node(6)
ju = Node(6)
ki = Node(6)
lo = Node(6)

aq.left = sw
aq.right = de
sw.left = fr
fr.right = gt
de.right = hy
de.left = ju
hy.right = ki
hy.left = lo

def LCA(curr, n1, n2):
    if curr == None:
        return None
    
    if curr == n1 or curr == n2:
        return curr

    left = LCA(curr.left, n1, n2)
    right = LCA(curr.right, n1, n2)

    if left != None and right != None:
        return curr


    return left if left else right

print LCA(aq, de, de) == aq
    
