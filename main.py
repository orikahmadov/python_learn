


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
                    
   


class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        new_node = BTNode(data)
        if self.root == None:
            self.root = new_node
        else:
            q = Queue()
            q.enqueue(self.root)
            while True:
                node = q.dequeue()
                if node.left == None:
                    node.left = new_node
                    return
                elif node.right == None:
                    node.right = new_node
                    return
                else:
                    q.enqueue(node.left)
                    q.enqueue(node.right)
                    
    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)
        
    def preorder(self, node):
        if node == None:
            return
        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)
        
    def postorder(self, node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)
        
    def levelorder(self):
        q = Queue()
        q.enqueue(self.root)
        while q.size() > 0:
            node = q.dequeue()
            print(node.data)
            if node.left != None:
                q.enqueue(node.left)
            if node.right != None:
                q.enqueue(node.right)
                
    def search(self, data):
        q = Queue()
        q.enqueue(self.root)
        while q.size() > 0:
            node = q.dequeue()
            if node.data == data:
                return True
            if node.left != None:
                q.enqueue(node.left)
            if node.right != None:
                q.enqueue(node.right)
        return False

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
        
class AVLTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        def insert_rec(node, data):
            if node == None:
                return AVLNode(data)
            if data < node.data:
                node.left = insert_rec(node.left, data)
            else:
                node.right = insert_rec(node.right, data)
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
            balance = self.getBalance(node)
            if balance > 1 and data < node.left.data:
                return self.rightRotate(node)
            if balance < -1 and data > node.right.data:
                return self.leftRotate(node)
            if balance > 1 and data > node.left.data:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)
            if balance < -1 and data < node.right.data:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)
            return node
        self.root = insert_rec(self.root, data)
        
    def getHeight(self, node):
        if node == None:
            return 0
        return node.height
    
    def getBalance(self, node):
        if node == None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y
    
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y
    
    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)
        
    def preorder(self, node):
        if node == None:
            return
        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)
        
    def postorder(self, node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)
        
    def levelorder(self):
        q = Queue()
        q.enqueue(self.root)
        while q.size() > 0:
            node = q.dequeue()
            print(node.data)
            if node.left != None:
                q.enqueue(node.left)
            if node.right != None:
                q.enqueue(node.right)
                
    def search(self, data):
        q = Queue()
        q.enqueue(self.root)
        while q.size() > 0:
            node = q.dequeue()
            if node.data == data:
                return True
            if node.left != None:
                q.enqueue(node.left)
            if node.right != None:
                q.enqueue(node.right)
        return False
    
    def delete(self, data):
        def delete_rec(node, data):
            if node == None:
                return node
            if data < node.data:
                node.left = delete_rec(node.left, data)
            elif data > node.data:
                node.right = delete_rec(node.right, data)
            else:
                if node.left == None:
                    temp = node.right
                    node = None
                    return temp
                elif node.right == None:
                    temp = node.left
                    node = None
                    return temp
                temp = self.minValueNode(node.right)
                node.data = temp.data
                node.right = delete_rec(node.right, temp.data)
            if node == None:
                return node
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
            balance = self.getBalance(node)
            if balance > 1 and self.getBalance(node.left) >= 0:
                return self.rightRotate(node)
            if balance < -1 and self.getBalance(node.right) <= 0:
                return self.leftRotate(node)
            if balance > 1 and self.getBalance(node.left) < 0:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)
            if balance < -1 and self.getBalance(node.right) > 0:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)
            return node
        self.root = delete_rec(self.root, data)
