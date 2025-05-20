#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        perimeter = 0
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 1: # if current cell is a land
                    perimeter += 4 # add 4 assuming each side unit length and we have no idea about neighboring cells.

                    # now, correct the assumed perimeter by actually checking the neighboring cells conditions
                    # since, we're traversing the matrix from left to right and then top to bottom, we only check 
                    # for right and the bottom neighbor and if they are lands, we subtract 2 each time
                    if col <= n_cols-2 and grid[row][col+1] == 1: # right neighbor
                        perimeter -= 2
                    if row <= n_rows-2 and grid[row+1][col] == 1: # bottom neighbor
                        perimeter -= 2
                    
        return perimeter
        
        # n_rows = len(grid)
        # n_cols = len(grid[0])

        # def dfs(row,col) -> int:
        #     # if the current cell is out of bounds or it is water then return 1
        #     if not (0 <= row < n_rows and 0 <= col < n_cols) or grid[row][col] == 0: return 1

        #     # if current cell is visited, return 0
        #     if grid[row][col] == -1: return 0
        #     grid[row][col] = -1 # else mark it as visited
        #     perimeter = 0
            
        #     for dr,dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, bottom, left, top
        #         perimeter += dfs(row+dr,col+dc) # accumulates the perimeter for the cell and returns that 
                
        #     return perimeter

        # for row in range(n_rows):
        #     for col in range(n_cols):
        #         if grid[row][col]:
        #             return dfs(row,col)

# @lc code=end
# asked in Amazon, Apple, Bloomberg, Facebook, Google, Microsoft