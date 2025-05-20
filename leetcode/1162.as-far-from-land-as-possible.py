#
# @lc app=leetcode id=1162 lang=python3
#
# [1162] As Far from Land as Possible
#
from typing import List
# @lc code=start
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c]==1:
                    q.append((r,c,0)) # row,col,dist_from_land
        
        if len(q) == 0 or len(q) == n*n:
            return -1 # if no land or water exists then return -1
        
        max_distance = 0
        while q:
            curr_r, curr_c, dist = q.popleft()
            max_distance = max(max_distance,dist)
            
            for dr,dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_r, new_c = curr_r+dr, curr_c+dc
                if 0<=new_r<n and 0<=new_c<n and grid[new_r][new_c]==0:
                    grid[new_r][new_c] = 1 # mark as visited by making it land
                    q.append((new_r,new_c,dist+1))

        return max_distance
# @lc code=end

