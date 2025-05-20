#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
from typing import List
# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n_rows = len(triangle)
        def recurse(r,c):
            if r == n_rows-1: return triangle[r][c] # only one base case because when moving vertically or diagonally below we won't run out of bounds except when last row which is handled here itself 
            down = triangle[r][c] + recurse(r+1,c)
            diag = triangle[r][c] + recurse(r+1,c+1)
            return min(down, diag)
        # return recurse(0,0) # TC: O(2^(1+2+3+...+n_rows)) 1st row has 1 col, 2nd has 2 cols, and so on until the last row has n cols and for each one of the cell we either move down or diag; SC: O(n_rows) - stack space is length of path which is number of rows 

        memo = {}
        def memoize(r,c):
            if (r,c) in memo: return memo[(r,c)]
            if r == n_rows-1: return triangle[r][c]
            down = triangle[r][c] + memoize(r+1,c)
            diag = triangle[r][c] + memoize(r+1,c+1)
            memo[(r,c)] = min(down, diag)
            return memo[(r,c)]
        # return memoize(0,0) # TC: O(n*n) where n=n_rows; SC: O(n) - recursion stack space

        def tabulation():
            dp = [[0]*n_rows for _ in range(n_rows)]
            for c in range(len(triangle[n_rows-1])): # fill last row of dp exactly as last row of trangle is
                dp[n_rows-1][c] = triangle[n_rows-1][c]

            for r in range(n_rows-2,-1,-1): # iterate from second last row to first to fill it from right to left
                for c in range(r,-1,-1):
                    down = triangle[r][c] + dp[r+1][c]
                    diag = triangle[r][c] + dp[r+1][c+1]
                    dp[r][c] = min(down,diag)
            return dp[0][0]
        # return tabulation() # TC: O(n*n), SC: O(n*n)

        def iteration():
            prev = [0]*n_rows
            for c in range(len(triangle[n_rows-1])):
                prev[c] = triangle[n_rows-1][c]

            for r in range(n_rows-2,-1,-1):
                temp = [0]*n_rows
                for c in range(r,-1,-1):
                    down = triangle[r][c] + prev[c]
                    diag = triangle[r][c] + prev[c+1]
                    temp[c] = min(down,diag)
                prev = temp
            return prev[0]
        return iteration() # TC: O(n*n), SC: O(n)

# @lc code=end

#  Amazon, Apple, Bloomberg, Google, Houzz 


