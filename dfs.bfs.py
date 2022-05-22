from collections import deque
 
class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
            
def recursiveBFS(graph, q, discovered):
 
    if not q:
        return
    v = q.popleft()
    print(v, end=' ')
    
    for u in graph.adjList[v]:
        if not discovered[u]:
            discovered[u] = True
            q.append(u)
 
    recursiveBFS(graph, q, discovered)
    
def DFS(graph, v, discovered):
    discovered[v] = True     
    print(v, end=' ')              

    for u in graph.adjList[v]:
        if not discovered[u]:    
            DFS(graph, u, discovered)
 
 
if __name__ == '__main__':
    edges = [
        (0,1), (0,2), (1,3), (1,4), (3,5), (5, 4),
        (4,2), (3,4)
    ]
    n = 6
    graph = Graph(edges, n)
 
    discovered = [False] * n
    
    ch=int(input("Select 1.DFS or 2.BFS := "))
    if(ch==1):
        for i in range(n):
            if not discovered[i]:
                DFS(graph, i, discovered)
    elif(ch==2):
        q = deque()
        for i in range(n):
            if not discovered[i]:
                discovered[i] = True
                q.append(i)
                recursiveBFS(graph, q, discovered) 
