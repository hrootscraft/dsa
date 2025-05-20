#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#
from typing import List
# @lc code=start
# Amazon, Bloomberg, Facebook, Google, LinkedIn, LiveRamp, Microsoft 
# props: if the graph is
#   1. linear - bipartite 
#   2. cyclic with even no.of nodes - bipartite
#   3. cyclic with odd no.of nodes - not bipartite
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [-1]*n # aka color array, we'll fill it with 0 and 1 representing the two colors 

        def dfs(i,color): # 0 - some color 1 (say, yellow) and 1 - some other color 2 (say green)
            visited[i] = color

            for neighbor in graph[i]:
                if visited[neighbor] == -1: # if the neighbor is not colored yet, run a dfs on it
                    if not dfs(neighbor, not color): return False 
                elif visited[neighbor] == color: return False # if the neighbor is visited and has the same color as it's edge's then it's not bipartite
            
            return True 

        # we may not necessarily have only a connected component in the graph    
        for node in range(n):
            if visited[node] == -1:
                # if any of the univisited component is not bipartite return False 
                if not dfs(node, 0): return False 
        return True # all the components are bipartite so return True
# @lc code=end

# Time Complexity: O(V + 2E), Where V = Vertices, 2E is for total degrees as we traverse all adjacent nodes.
# Space Complexity: O(2V) ~ O(V), Space for DFS stack space, visited array.
