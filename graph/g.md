
- made of nodes (n) and edges (m) 
- can be directed or undirected 
- can be cyclic (atleast one loop in the graph) or acyclic
- can have x number of connected components and remaining would be unconnected (traversal in this case would be done using a visited array with elements being the vertices)
- can be weighted (directed/undirected) graphs or unweighted (unit weights)
- tree is a spl. case of directed acyclic graphs
- graph can be represented using an adjacency matrix or an adjacency list 
- matrix takes O(n^2) space while list uses O(2*m) because for every edge you are storing 2 nodes (in an undirected graph)
- which to use? 

    1. if the graph is complete (ie we have maximum # of edges), use adj. matrix 'cause then we'll have more 1s (1 if the graph is not weighted, if weighted then that weight goes in both the cells)

    2. if the # of edges are less use adj. list (in python, we use dictionary with node as the key and list of its connected nodes as the value); in case of weighted graph, we store values in the dict as tuples with neighbor node and the corresponding weight {"a": [("b",2), ("c",3)]}