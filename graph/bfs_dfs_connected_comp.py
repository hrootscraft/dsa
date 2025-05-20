# graphs can be 1-index based (graph starts from 1) or 0-index based (graph starts from 0) 
# breadth first search (bfs) traversal aka level wise traversal  

# they'll give a starting node (only 1 node can be at level 0 ie only 1 node can be a starting node)
# then we can have multiple nodes starting from level 2
# from the starting node you need to print your graph level wise

#         ________1______
#        |               |
#     ___2___         ___6___
#    |       |       |       |
#    3    ___4       7___    9
#        |               |
#        5_______________8

# Pseudo Code :
# 1. init a boolean array with False (unvisited) & of size n where n->no.of nodes in the graph
# 2. init an empty queue (for bfs)
# 3. push the starting node in the queue
# 4. mark it as visited (True) in the array
# 5. while the queue is not empty:
# 6.      pop the first element in the queue 
# 7.      add the "unvisited" neighbors of this popped item in the queue
# 8.      mark the neighbors as visited

from typing import Optional, Any, Set
from collections import defaultdict, deque

class Graph: # creates undirected unweighted graphs
    def __init__(self, graph: Optional[dict[Any, Set[Any]]] = None) -> None:
        self.graph = defaultdict(set, graph if graph is not None else {})

    def addVertex(self, vertex: Any) -> None:
        if vertex not in self.graph: 
            self.graph[vertex] = set()

    def addEdge(self, vertex, neighbor):
        self.graph[vertex].add(neighbor)
        self.graph[neighbor].add(vertex)

    def __str__(self) -> str:
        return "\n".join([f"{vertex}: {neighbors}" for vertex, neighbors in self.graph.items()])

    # TC: O(n) + O(2*e) ie computations for all the vertices and for every vertex, the # of degrees which is 2*e
    # here n is the # of vertices and e is the # of edges
    def BFS(self, start_vertex):
        visited = [False]* (max(self.graph)+1) # assuming the keys are array indexed
        queue = []
        queue.append(start_vertex) 
        visited[start_vertex] = True

        while queue:
            curr_vertex = queue.pop(0) # assign the current vertex with the first element from the queue and remove it 
            print(curr_vertex, end=" ")
            for neighbor in self.graph[curr_vertex]:
                if visited[neighbor] == False:
                    queue.append(neighbor) # add the unvisited to the queue
                    visited[neighbor] = True # and mark it as visited

    def pythonic_BFS(self, start_vertex): # default is iterative
        visited = set() # checking if an element is in a set - TC: O(1)
        queue = deque([start_vertex]) # FIFO: append from the right, remove from the left
        visited_order = [] 

        while queue: 
            curr_vertex = queue.popleft()
            if curr_vertex not in visited:
                visited_order.append(curr_vertex)
                visited.add(curr_vertex)
                queue.extend(self.graph[curr_vertex])
        return visited_order

    # same as above but has just used a stack 
    def pythonic_iterative_DFS(self, start_vertex): 
        visited = set()
        stack = deque([start_vertex]) # LIFO: append from the right, remove from the right
        visited_order = []

        while stack:
            curr_vertex = stack.pop() # get the last element to explore
            if curr_vertex not in visited: # if that element is not visited 
                visited_order.append(curr_vertex) # and process it 
                visited.add(curr_vertex) # mark it as visited
                stack.extend(self.graph[curr_vertex])
        return visited_order        
    
    def recursive_DFS(self, start_vertex) -> list: # SC: O(n), TC: O(n+2*e) ## for directed graph it'll be e instead of 2*e
        visited = set()
        visited_order = []

        def dfs(node) -> None:
            visited.add(node) # mark the current node as visited
            visited_order.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start_vertex)
        return visited_order  
    
    def n_connected_components(self):
        visited = set()
        n_components = 0

        def dfs(node):
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for key in self.graph:
            if key not in visited:
                dfs(key)
                n_components += 1
        
        return n_components
    
    def n_connected_components_arr(self): # SC: O(n), TC: O(n)+O(n+2*e)
        n_nodes = len(self.graph)
        visited = [False]*(n_nodes+1)
        n_components = 0

        def dfs(node):
            visited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        for i in range(1,n_nodes+1):
            if not visited[i]:
                dfs(i) 
                n_components += 1
        
        return n_components
    
# g = Graph()
# g.addEdge(1,2)
# g.addEdge(1,6)
# g.addEdge(2,3)
# g.addEdge(2,4)
# g.addEdge(4,5)
# g.addEdge(5,8)
# g.addEdge(6,7)
# g.addEdge(6,9)
# g.addEdge(7,8)

# print(g.graph)
# print(g.pythonic_BFS(1))
# print(g.BFS(1))
# # print(g.pythonic_BFS(7))
# print(g.pythonic_iterative_DFS(1))

# # driver code
# graph = {
#     1: {2,6},
#     2: {1,3,4},
#     3: {2},
#     4: {2,5},
#     5: {4,8},
#     6: {1,7,9},
#     7: {6,8},
#     8: {5,7},
#     9: {6},
# }
# gg = Graph(graph)
# print(gg.pythonic_BFS(1))

# when traversing an undirected graph, you might end up at 
# the same node and so a visited array is needed
# whereas for a tree, such an array is not needed

# g_dfs = Graph()
# g_dfs.addEdge(1,2)
# g_dfs.addEdge(1,3)
# g_dfs.addEdge(2,5)
# g_dfs.addEdge(2,6)
# g_dfs.addEdge(3,4)
# g_dfs.addEdge(3,7)
# g_dfs.addEdge(4,8)
# g_dfs.addEdge(7,8)
# print(g_dfs)
# print(g_dfs.recursive_DFS(1))

cc_g = Graph()
cc_g.addEdge(1,2)
cc_g.addEdge(2,3)
cc_g.addEdge(2,4)
cc_g.addEdge(3,5)
cc_g.addEdge(6,7)   
cc_g.addVertex(8)
print(cc_g.n_connected_components())
print(cc_g.n_connected_components_arr())

