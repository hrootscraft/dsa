#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
from typing import List
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        memo = {}
        def recurse(r,c):
            if r==0 and c==0: return grid[0][0] # if we reach here, we add it to the path
            if r<0 or r>n_rows-1 or c<0 or c>n_cols-1: return float("inf") # if a cell out of bounds is reached, return something so that the current path_sum is not considered; hence, we return infinty
            up = grid[r][c] + recurse(r-1,c)
            left = grid[r][c] + recurse(r,c-1)
            return min(up,left)
        # return recurse(n_rows-1,n_cols-1)

        def memoize(r,c):
            if (r,c) in memo: return memo[(r,c)]
            if r==0 and c==0: return grid[0][0]
            if r<0 or r>n_rows-1 or c<0 or c>n_cols-1: return float("inf")
            up = grid[r][c] + memoize(r-1,c)
            left = grid[r][c] + memoize(r,c-1)
            memo[(r,c)] = min(up,left)
            return memo[(r,c)]
        # return memoize(n_rows-1,n_cols-1)

        def tabulation():
            dp = [[0]*n_cols for _ in range(n_rows)]
            for r in range(n_rows):
                for c in range(n_cols):
                    if r==0 and c==0: # base case: if at the top-left corner, set dp[r][c] to the value of that cell
                        dp[r][c] = grid[0][0]
                        continue

                    up = grid[r][c] 
                    if r>0: up += dp[r-1][c]
                    else: up += float("inf")

                    left = grid[r][c] 
                    if c>0: left += dp[r][c-1]
                    else: left += float("inf")

                    dp[r][c] = min(up,left)

            return dp[n_rows-1][n_cols-1]
        # return tabulation()

        def iteration():
            prev = [0]*n_cols
            for r in range(n_rows):
                temp = [0]*n_cols
                for c in range(n_cols):
                    if r==0 and c==0: 
                        temp[c] = grid[0][0]
                        continue

                    up = grid[r][c] 
                    if r>0: up += prev[c]
                    else: up += float("inf")

                    left = grid[r][c] 
                    if c>0: left += temp[c-1]
                    else: left += float("inf")

                    temp[c] = min(up,left)
                prev = temp
            return prev[n_cols-1]
        return iteration()

# @lc code=end

#  Adobe, Amazon, Apple, Bloomberg, Dropbox, Goldman Sachs, Google, Microsoft, Nvidia, Rubrik, Uber 