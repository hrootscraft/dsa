# M-coloring problem: given an undirected graph and an integer M, tell 
# whether the graph nodes can be colored with at most M distinct colors such 
# that no two adjacent nodes have the same color 

# Input:
# N = 4
# M = 3
# E = 5
# Edges[] = {(0,1),(1,2),(2,3),(3,0),(0,2)}
# Output: 1
# Explanation: It is possible to colour the
# given graph using 3 colours.

# Input:
# N = 3
# M = 2
# E = 3
# Edges[] = {(0,1),(1,2),(0,2)}
# Output: 0
from collections import defaultdict

def build_graph(edges):
    g = defaultdict(set)
    for v1,v2 in edges:
        g[v1].add(v2)
        g[v2].add(v1)
    return g

def solve(n,m,e,edges):
    g = build_graph(edges)
    colors = [-1]*n # this also acts as visited array for the n nodes ie if it is already colored then it is visited
    
    def is_possible_to_color(curr_node,color):
        for neighbor in g[curr_node]:
            if colors[neighbor] == color: return False
        return True 

    def recurse(curr_node):
        # if you get past the last node by coloring all previous 
        # nodes abiding by the previous conditions, return true
        if curr_node == n: return True 

        # if the curr_node is anything except last one, then we try and color it
        for color in range(m):
            if is_possible_to_color(curr_node,color): 
                colors[curr_node] = color # assign the color and go to color next node
                if recurse(curr_node+1): return True # if this is not possible, then undo the assigned color
                colors[curr_node] = -1 # mark it unvisited | backtrack

        return False # all nodes are exhausted and no true was returned 

    if recurse(0): return True 
    return False

n=4 # no.of nodes starting from 0 to n-1
m=3 # no.of colors
e=5 # no.of edges
edges = [(0,1),(1,2),(2,3),(3,0),(0,2)]

print(solve(n,m,e,edges))

n=3 # no.of nodes starting from 0 to n-1
m=2 # no.of colors
e=3 # no.of edges
edges = [(0,1),(1,2),(0,2)]

print(solve(n,m,e,edges))

## TC: O(n^m)
## SC: O(n) + O(n) - colors array and recursion stack
