import datetime
import time
class Node:
    def __init__(self,data):
        self.data = data
        self.neighbors = []


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)

a.neighbors.extend([(b, 2), (c,5), (d,3)])
b.neighbors.extend([(a,2),(c,1), (e,34), (f,1)])
c.neighbors.extend([(a, 5),(b,1),(h,52)])
d.neighbors.extend([(a, 3), (e,30), (g, 20)])
e.neighbors.extend([(b, 34),(d,30)])
f.neighbors.extend([(b,1),(g,12)])
g.neighbors.extend([(d,20), (f,12)])
h.neighbors.extend([(c,52)])

def dijkstra(root):
    queue = []
    #count = 0

    queue.append(([root], 0))
    distances = {root: ([], 0)}

    while len(queue) > 0:
        #count += 1
        path, length = queue.pop(0)
        node = path[-1]
        if distances[node] >= length:
            for n in node.neighbors:
                if n[0] not in distances:
                    distances[n[0]] = (path + [n[0]], length + n[1])
                    queue.append((path + [n[0]], length + n[1]))
                elif length + n[1] < distances[n[0]][1]:
                    distances[n[0]] = (path + [n[0]], length + n[1])
                    queue.append((path + [n[0]], length + n[1]))
    
    return distances

start = time.time()
distances = dijkstra(d)
end = time.time()
print end - start
print distances[h][1]