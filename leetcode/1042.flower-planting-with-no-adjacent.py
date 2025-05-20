#
# @lc app=leetcode id=1042 lang=python3
#
# [1042] Flower Planting With No Adjacent
#
from typing import List

# @lc code=start
from collections import defaultdict
# linkedin # ~ m_coloring problem asked in amazon 
class Solution:
    def build_graph(self, edges):
        g = defaultdict(list)
        for v1,v2 in edges:
            g[v1].append(v2)
            g[v2].append(v1)
        return g      

    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        g = self.build_graph(paths)
        n_colors = 4
        colors = [-1]*(n+1) # represents the flowers 

        def is_possible_to_color(curr_node,color):
            for neighbor in g[curr_node]:
                if colors[neighbor] == color: return False
            return True

        def recurse(curr_node): # garden is the node
            if curr_node == n+1: return True
            
            for color in range(1,n_colors+1):
                if is_possible_to_color(curr_node,color): 
                    colors[curr_node] = color 
                    if recurse(curr_node+1): return True 
                    colors[curr_node] = -1 

            return False # all nodes are exhausted and no true was returned 

        if recurse(0): return colors[1:]
        return []

# @lc code=end

