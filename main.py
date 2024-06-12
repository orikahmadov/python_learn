


class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    def display(self):
        print(self.queue)
    def size(self):
        return len(self.queue)
    
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()
    def display(self):
        print(self.stack)
    def size(self):
        return len(self.stack)
    
class Graph:
    def __init__(self):
        self.graph = {}
        
    def addEdge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)
    def display(self):
        print(self.graph)
        
    def BFS(self, start):
        visited = []
        q = Queue()
        q.enqueue(start)
        visited.append(start)
        while q.size() > 0:
            node = q.dequeue()
            print(node)
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    q.enqueue(neighbour)
                    visited.append(neighbour)
    def DFS(self, start):
        """
        Performs a Depth-First Search (DFS) traversal starting from the given start node.

        Parameters:
        - start: The starting node for the DFS traversal.

        Returns:
        None

        """
        visited = []
        s = Stack()
        s.push(start)
        visited.append(start)
        while s.size() > 0:
            node = s.pop()
            print(node)
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    s.push(neighbour)
                    visited.append(neighbour)
                    
   


g = Graph()
g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'D')
g.addEdge('B', 'E')
g.addEdge('C', 'F')
g.addEdge('C', 'G')
g.addEdge('D', 'H')
g.addEdge('D', 'I')

g.display()