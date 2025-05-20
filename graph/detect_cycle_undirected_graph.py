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
    
    def is_cyclic_bfs(self, src) -> bool: # does the undirected graph contain a cycle?
        # the intuition here would be if a bfs starts from point and then collides 
        # at the some other point further down the traversal, then there is a cycle 
        visited = set()
        q = deque([(src,-1)]) # (vertex,parent_vertex)
        visited.add(src) 
        while q:
            curr_vertex, curr_vertex_parent = q.popleft()
            for neighbor in self.graph[curr_vertex]: 
                if neighbor not in visited: # if the neighbor of current vertex, mark it as visited 
                    visited.add(neighbor)
                    q.append((neighbor, curr_vertex))
                elif curr_vertex_parent != neighbor: # if the neighbor is already visited (this can happen when one bfs call reaches the node earlier than the other bfs call in a cycle)
                # And it is not the parent, we have encountered a cycle (basically, if a node is visited and it did not from it's parent then there's a cycle)
                    return True
        return False
    
    def is_cyclic_bfs_disconnected_components(self) -> bool:
        visited = set()
        for node in self.graph:
            if node not in visited:
                visited.add(node)
                if self.is_cyclic_bfs(node): return True
        return False
    
    def is_cyclic_dfs(self, src) -> bool:
        visited = set()

        def dfs(curr_vertex,curr_vertex_parent) -> bool:
            visited.add(curr_vertex)
            for neighbor in self.graph[curr_vertex]:
                if neighbor not in visited:
                    if dfs(neighbor, curr_vertex): return True 
                elif curr_vertex_parent != neighbor: return True # when the neighbor is already visited but it does not come from the parent then we have a cycle
            return False
    
        return dfs(src,-1)
    
    def is_cyclic_dfs_disconnected_components(self) -> bool:
        visited = set()
        for node in self.graph:
            if node not in visited:
                visited.add(node)
                if self.is_cyclic_dfs(node): return True
        return False

g = Graph()
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(3,4)
g.addEdge(2,5)
g.addEdge(3,6)
g.addEdge(5,7)
g.addEdge(6,7)
# print(g)
# print(g.is_cyclic_bfs(1))
# print(g.is_cyclic_bfs(4))
# print(g.is_cyclic_dfs(4))

g_discon = Graph()
g_discon.addEdge(1,3)
g_discon.addEdge(1,2)
g_discon.addEdge(2,4)
g_discon.addEdge(5,6)
g_discon.addEdge(8,9)
g_discon.addEdge(8,7)
# g_discon.addEdge(9,7) # uncomment this to get a cycle
print(g_discon)
print(g_discon.is_cyclic_bfs_disconnected_components())
print(g_discon.is_cyclic_dfs_disconnected_components())

## TC: O(n+2e)
## SC: O(n)