from typing import Optional, Any, Set
from collections import defaultdict

class BaseGraph:
    def __init__(self, graph: Optional[dict[Any, Set[Any]]] = None) -> None:
        self.graph = defaultdict(set, graph if graph is not None else {})

    def addVertex(self, vertex: Any) -> None:
        if vertex not in self.graph: 
            self.graph[vertex] = set()

    def __str__(self) -> str:
        return "\n".join([f"{vertex}: {neighbors}" for vertex, neighbors in self.graph.items()])
    
class UndirectedGraph(BaseGraph):   
    def addEdge(self, vertex: Any, neighbor: Any, weight: Optional[int] = None) -> None:
        self.addVertex(vertex)
        self.addVertex(neighbor)
        # self.graph[vertex].add((neighbor, weight))
        # self.graph[neighbor].add((vertex, weight))

        if weight is None:  # Unweighted graph
            self.graph[vertex].add(neighbor)  
            self.graph[neighbor].add(vertex)
        else:  # Weighted graph
            self.graph[vertex].add((neighbor, weight))
            self.graph[neighbor].add((vertex, weight))

    def removeEdge(self, vertex: Any, neighbor: Any) -> None:
        if vertex in self.graph and neighbor in self.graph:
            # Check if the first element in the set is a tuple (indicates weighted graph)
            is_weighted = isinstance(next(iter(self.graph[vertex])), tuple)

            if is_weighted:
                # Weighted graph: remove (neighbor, weight) tuple
                self.graph[vertex] = {(n, w) for n, w in self.graph[vertex] if n != neighbor}
                self.graph[neighbor] = {(n, w) for n, w in self.graph[neighbor] if n != vertex}
            else:
                # Unweighted graph: discard neighbor
                self.graph[vertex].discard(neighbor)
                self.graph[neighbor].discard(vertex)
    
    def removeVertex(self, vertex: Any):
        # when removing a vertex, we first need to delete the edge between that neighbor and it's adjacent vertex in it's set
        # eg. in {
        #   A: [B,C,D],
        #   B: [A,C],
        #   C: [A,B,D],
        #   D: [A,C]
        # } when removing the vertex D, we first need to loop through the neigbors [A,C] and delete those edges with the vertex ie A-D and C-D 
        if vertex in self.graph:
            is_weighted = isinstance(next(iter(self.graph[vertex])), tuple)
            if is_weighted:
                for (n,w) in self.graph[vertex].copy():
                    self.removeEdge(n,vertex)
            else:
            # Create a copy of neighbors before iterating because you cannot iterate and delete it'll arise an anomaly
                neighbors_to_remove = list(self.graph[vertex])
                for v in neighbors_to_remove:
                    self.removeEdge(v,vertex)
            del self.graph[vertex]


class DirectedGraph(BaseGraph):
    def addEdge(self, vertex: Any, neighbor: Any, weight: Optional[int] = None) -> None:
        # self.addVertex(vertex)
        # self.addVertex(neighbor)
        if vertex not in self.graph:
            self.graph[vertex] = set()  # Initialize only when adding an edge
        # self.graph[vertex].add((neighbor, weight))
            
        if weight is None:  # Unweighted graph
            self.graph[vertex].add(neighbor)  
        else:  # Weighted graph
            self.graph[vertex].add((neighbor, weight))

    def removeEdge(self, vertex: Any, neighbor: Any) -> None:
        if vertex in self.graph:
            is_weighted = isinstance(next(iter(self.graph[vertex])), tuple)
            if is_weighted:
                self.graph[vertex] = {(n, w) for n, w in self.graph[vertex] if n != neighbor}
            else:
                self.graph[vertex].discard(neighbor)

    def removeVertex(self, vertex: Any):
        neighbors_to_remove = list(self.graph[vertex])
        for v in neighbors_to_remove:
            self.removeEdge(v,vertex)
        del self.graph[vertex]

## Driver code
# unweighted_undirected_g = UndirectedGraph()
# unweighted_undirected_g.addVertex("a")
# print(f"Unweighted Undirected Graph : \n{unweighted_undirected_g}")
# unweighted_undirected_g.addEdge("a","b")
# unweighted_undirected_g.addEdge("a","c")
# unweighted_undirected_g.addEdge("a","d")
# unweighted_undirected_g.addEdge("c","b")
# unweighted_undirected_g.addEdge("c","d")
# unweighted_undirected_g.addEdge("d","e")
# print(f"Unweighted Undirected Graph : \n{unweighted_undirected_g}")
# unweighted_undirected_g.removeEdge('e','d')
# print(f"Unweighted Undirected Graph : \n{unweighted_undirected_g}")
# unweighted_undirected_g.removeVertex("d")
# print(f"Unweighted Undirected Graph : \n{unweighted_undirected_g}")

# weighted_undirected_g = UndirectedGraph()
# weighted_undirected_g.addVertex("a")
# print(f"Weighted Undirected Graph : \n{weighted_undirected_g}")
# weighted_undirected_g.addEdge("a","b", 10)
# weighted_undirected_g.addEdge("a","f", 20)
# weighted_undirected_g.addEdge("c","d", 5)
# print(f"Weighted Undirected Graph : \n{weighted_undirected_g}")
# weighted_undirected_g.removeEdge("c", "d")
# print(f"Weighted Undirected Graph : \n{weighted_undirected_g}")
# weighted_undirected_g.removeVertex("a")
# print(f"Weighted Undirected Graph : \n{weighted_undirected_g}")

# unweighted_directed_g = DirectedGraph()
# unweighted_directed_g.addVertex("a")
# print(f"Unweighted Directed Graph : \n{unweighted_directed_g}")
# unweighted_directed_g.addEdge("a","b")
# unweighted_directed_g.addEdge("c","d")
# unweighted_directed_g.addEdge("c","e")
# print(f"Unweighted Directed Graph : \n{unweighted_directed_g}")
# unweighted_directed_g.removeEdge("c","e")
# print(f"Unweighted Directed Graph : \n{unweighted_directed_g}")

# weighted_directed_g = DirectedGraph()
# weighted_directed_g.addVertex("a")
# print(f"Weighted Directed Graph : \n{weighted_directed_g}")
# weighted_directed_g.addEdge("a","b", 10)
# weighted_directed_g.addEdge("a","f", 20)
# weighted_directed_g.addEdge("c","d", 5)
# weighted_directed_g.addEdge("c","g", 15)
# print(f"Weighted Directed Graph : \n{weighted_directed_g}")
# weighted_directed_g.removeEdge("c","g")
# print(f"Weighted Directed Graph : \n{weighted_directed_g}")
# weighted_directed_g.removeEdge("c","d")
# print(f"Weighted Directed Graph : \n{weighted_directed_g}")

# custom_graph_unweighted_undirected = {
#     "a": {"b","c"},
#     "b": {"a","d","e"},
#     "c": {"a","e"},
#     "d": {"b","e","f"},
#     "e": {"b","f","c","d"},
#     "f": {"d","e"},
# }
# uw_ud = UndirectedGraph(custom_graph_unweighted_undirected)
# print(f"Unweighted Undirected Graph : \n{uw_ud}")
# uw_ud.addEdge("e","a")
# print(f"Unweighted Undirected Graph : \n{uw_ud}")
    
# custom_graph_weighted_undirected = {
#     "a": {("b",10),("c",20)},
#     "b": {("a",10),("d",30),("e",40)},
#     "c": {("a",20),("e",50)},
#     "d": {("b",30),("e",60),("f",70)},
#     "e": {("b",40),("f",80),("c",50),("d",60)},
#     "f": {("d",70),("e",80)},
# }
# w_ud = UndirectedGraph(custom_graph_weighted_undirected)
# print(f"Weighted Undirected Graph : \n{w_ud}")
# w_ud.addEdge("e","a", 17)
# print(f"Weighted Undirected Graph : \n{w_ud}")

# custom_graph_unweighted_directed = {
#     "a": {"b","c"},
#     "b": {"d","e"},
#     "c": {"e"},
#     "d": {"e","f"},
#     "e": {"f"},
# }
# uw_d = DirectedGraph(custom_graph_unweighted_directed)
# print(f"Unweighted Directed Graph : \n{uw_d}")
# uw_d.addEdge("e","g")
# print(f"Unweighted Directed Graph : \n{uw_d}")

# custom_graph_weighted_directed = {
#     "a": {("b",10),("c",20)},
#     "b": {("d",30),("e",40)},
#     "c": {("e",50)},
#     "d": {("e",60),("f",70)},
#     "e": {("f",80)},
# }
# w_d = DirectedGraph(custom_graph_weighted_directed)
# print(f"Weighted Directed Graph : \n{w_d}")
# w_d.addEdge("e","a", 17)
# print(f"Weighted Directed Graph : \n{w_d}")