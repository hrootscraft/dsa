#
# @lc app=leetcode id=1463 lang=python3
#
# [1463] Cherry Pickup II
#
from typing import List

# @lc code=start
# Google
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])

        def recurse(r,c1,c2):
            if c1 < 0 or c2 < 0 or c1 >= n_cols or c2 >= n_cols:
                return float('-inf')

            if r == n_rows - 1:
                return grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]

            main_max = float("-inf")

            for i in range(-1,2): 
                for j in range(-1,2): 
                    newc_1, new_c2 = c1+i, c2+j
                    if 0 <= newc_1 < n_cols and 0 <= new_c2 < n_cols:
                        curr_sum = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]
                        main_max = max(main_max, curr_sum+recurse(r+1, newc_1, new_c2))
            return main_max
        
        # return recurse(0,0,n_cols-1)

        memo = {}
        def memoize(r,c1,c2):
            if (r,c1,c2) in memo: return memo[(r,c1,c2)]
            if c1<0 or c2<0 or c1>=n_cols or c2>=n_cols: return float('-inf')
            if r==n_rows-1: return grid[r][c1] if c1==c2 else grid[r][c1]+grid[r][c2]

            main_max = float("-inf")
            for i in range(-1,2): 
                for j in range(-1,2): 
                    newc_1, new_c2 = c1+i, c2+j
                    if 0 <= newc_1 < n_cols and 0 <= new_c2 < n_cols:
                        curr_sum = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]
                        main_max = max(main_max, curr_sum+memoize(r+1, newc_1, new_c2))
                        
            memo[(r,c1,c2)] = main_max
            return main_max
        
        return memoize(0,0,n_cols-1)

# @lc code=end

