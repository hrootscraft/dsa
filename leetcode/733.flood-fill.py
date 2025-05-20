#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
from typing import List
# from copy import deepcopy
from collections import deque

class Solution:
    # in the industry, you don't tamper with the data so it is advised to make a 
    # deep copy of the image to modify it & return that itself. however, in the following solution 
    # we have modified the image itself for better performance on leetcode 
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n_rows, n_cols = len(image), len(image[0])
        init_color = image[sr][sc]
        if init_color == color:  # if the color is the same, no need to proceed
            return image

        def dfs(row, col):
            if not (0 <= row < n_rows and 0 <= col < n_cols) or image[row][col] != init_color:
                return
            image[row][col] = color
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # right, bottom, left, top
                dfs(row + dr, col + dc)

        dfs(sr, sc)
        return image
        
        # n_rows = len(image)
        # n_cols = len(image[0])
        # delta_row = [-1, 0, +1, 0]
        # delta_col = [0, +1, 0, -1]
        # init_color = image[sr][sc]

        # def dfs(row, col):
        #     image[row][col] = color
            
        #     for i in range(4):
        #         new_row, new_col = row+delta_row[i], col+delta_col[i] 
        #         if 0 <= new_row < n_rows and 0 <= new_col < n_cols and image[new_row][new_col] == init_color:
        #             dfs(new_row,new_col)

        # if image[sr][sc] == color:
        #     return image
        # dfs(sr,sc)
        # return image
    
    # def floodFillWithBfs(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    #     n_rows, n_cols = len(image), len(image[0])
    #     init_color = image[sr][sc]
    #     if init_color == color:  # if the color is the same, no need to proceed
    #         return image

    #     queue = deque([(sr, sc)])
    #     visited = set([(sr, sc)])  # track visited pixels

    #     while queue:
    #         row, col = queue.popleft()
    #         image[row][col] = color
    #         for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, bottom, left, top
    #             new_row, new_col = row + dr, col + dc
    #             if (0 <= new_row < n_rows and 0 <= new_col < n_cols and image[new_row][new_col] == init_color and (new_row, new_col) not in visited):
    #                 queue.append((new_row, new_col))
    #                 visited.add((new_row, new_col))

    #     return image
        
# @lc code=end
