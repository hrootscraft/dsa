#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#
from typing import List
# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        memo = {}

        def recurse(r,c): # TC: for every cell in a path, 3 directions are explored so O(n_cols*(3^n_rows); SC: the depth of the recursion is O(n_rows)
            if c<0 or c>n_cols-1: return float("inf")
            if r == 0: return matrix[r][c]
            left_diag_up = matrix[r][c] + recurse(r-1,c-1) 
            up = matrix[r][c] + recurse(r-1,c)
            right_diag_up = matrix[r][c] + recurse(r-1,c+1) 
            return min(left_diag_up, up, right_diag_up)
        
        def memoize(r,c): # TC: for every cell in last row we call the recursive function and each of this function makes 3 other calls if it is not memoized so TC is O(n_rows*n_cols) as each cell is computed only once; SC: memo table can have atmost all cells so O(n_rows*n_cols) and for recursion stack O(n_rows) 
            if (r,c) in memo: return memo[(r,c)]
            if c<0 or c>n_cols-1: return float("inf")
            if r == 0: return matrix[r][c]
            left_diag_up = matrix[r][c] + memoize(r-1,c-1) 
            up = matrix[r][c] + memoize(r-1,c)
            right_diag_up = matrix[r][c] + memoize(r-1,c+1) 
            memo[(r,c)] = min(left_diag_up, up, right_diag_up)
            return memo[(r,c)]
            
        def tabulation(): # TC: O(n_rows*n_cols), SC: O(n_rows*n_cols)
            dp = [[0]*n_cols for _ in range(n_rows)]
            # init first row with base condition
            for c in range(n_cols):
                dp[0][c] = matrix[0][c]

            # iterate through the matrix from 2nd row to compute for each cell
            for r in range(1,n_rows):
                for c in range(n_cols):
                    up = matrix[r][c] + dp[r-1][c]

                    left_diag_up = matrix[r][c] 
                    if c-1 >= 0: left_diag_up += dp[r-1][c-1]
                    else: left_diag_up += float("inf")

                    right_diag_up = matrix[r][c] 
                    if c+1<n_cols: right_diag_up += dp[r-1][c+1]
                    else: right_diag_up += float("inf")

                    dp[r][c] = min(up, left_diag_up, right_diag_up)

            main_min = float("inf")
            for col in range(n_cols):
                main_min = min(main_min, dp[n_rows-1][col]) # constant time operation 

            return main_min
        # return tabulation()

        def iteration(): # TC: O(n_rows*n_cols), SC: O(n_cols)
            prev = [0]*n_cols
            for c in range(n_cols):
                prev[c] = matrix[0][c]

            for r in range(1,n_rows):
                temp = [0]*n_cols
                for c in range(n_cols):
                    up = matrix[r][c] + prev[c]

                    left_diag_up = matrix[r][c] 
                    if c-1 >= 0: left_diag_up += prev[c-1]
                    else: left_diag_up += float("inf")

                    right_diag_up = matrix[r][c] 
                    if c+1<n_cols: right_diag_up += prev[c+1]
                    else: right_diag_up += float("inf")

                    temp[c] = min(up, left_diag_up, right_diag_up)
                prev = temp
                
            main_min = float("inf")
            for col in range(n_cols):
                main_min = min(main_min, prev[col])
            return main_min
        
        return iteration()

        # main_min = float("inf")
        # for col in range(n_cols):
        #     # main_min = min(main_min, recurse(n_rows-1,col))
        #     # main_min = min(main_min, memoize(n_rows-1,col))
        # return main_min

# @lc code=end

#  Goldman Sachs, Google 