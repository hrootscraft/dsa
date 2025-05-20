dir_graph = [[], [2], [3], [4, 7], [5], [6], [], [5], [9], [10], [8]] 
# here, index i represents the node and graph[i] represents the nodes that it is connected to.
# so, 1 is connected to 2, 3 is connected to both 4 and 7, ...

def detect_cycle(g):
    visited = set()
    path_visited = set()

    def dfs(node):
        visited.add(node)
        path_visited.add(node)

        for neighbor in g[node]:
            if neighbor not in visited:
                if dfs(neighbor): return True
                elif neighbor in path_visited: return True 

        path_visited.remove(node) # when returning you remove the node from the path visited
        return False # no cycle found

    for node in range(len(g)): # similar to what's done for unconnected components, call dfs from each unvisited node
        if node not in visited:
            if dfs(node): return True # if you find a cycle when starting dfs with a node, return True

    return False # if there is no cycle found after visiting all nodes, return False

print(detect_cycle(dir_graph)) # WRING ANSWER