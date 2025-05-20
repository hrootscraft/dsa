#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
from typing import List
# @lc code=start

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n_rows = len(mat)
        n_cols = len(mat[0])
        distance_mat = [[-1]*n_cols for _ in range(n_rows)] # also serves as visited matrix
        queue = deque()

        # add all 0s to the queue and update their distances
        for r in range(n_rows):
            for c in range(n_cols):
                if mat[r][c] == 0: 
                    queue.append((r,c))
                    distance_mat[r][c] = 0

        while queue:
            curr_r, curr_c = queue.popleft()
            # for all neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r, new_c = curr_r+dr, curr_c+dc
                # if the neighbors are within bounds and not visited ie distance is still -1 then we take 1 step
                if (0<=new_r<n_rows and 0<=new_c<n_cols) and distance_mat[new_r][new_c] == -1:
                    distance_mat[new_r][new_c] = distance_mat[curr_r][curr_c] + 1
                    queue.append((new_r,new_c))

        return distance_mat
    
# @lc code=end
# Time complexity: O(m∗n)
# Space complexity: O(m∗n)