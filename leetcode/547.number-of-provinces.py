#
# @lc app=leetcode id=51 lang=python3
#
# [547] Number of Provinces
#
from collections import deque
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n_provinces = 0
        visited = set()

        def dfs(city):
            visited.add(city)
            for neighbor, connected in enumerate(isConnected[city]):
                if connected and neighbor not in visited:
                    dfs(neighbor)

        # def bfs(start_city):
        #     queue = deque([start_city])
        #     while queue:
        #         city = queue.popleft()
        #         visited.add(city)
        #         for neighbor, connected in enumerate(isConnected[city]): # enumerate returns (index,value)
        #             if connected and neighbor not in visited:
        #                 queue.append(neighbor)

        for city in range(len(isConnected)):
            if city not in visited:
                dfs(city) # bfs(city)
                n_provinces += 1

        return n_provinces
    
# @lc code=end

        # # n_cities = len(isConnected)
        # visited, n_provinces = set(), 0

        # def dfs(i):
        #     visited.add(i)
        #     for j in range(len(isConnected)):
        #         # if j is the neighbor of i and it is not visited, then explore j and mark it as visited
        #         if j not in visited and isConnected[i][j]:
        #             visited.add(j)
        #             dfs(j)

        # for i in range(len(isConnected)):
        #     if i not in visited:
        #         dfs(i) # explore city i
        #         n_provinces += 1
          
        # return n_provinces
    