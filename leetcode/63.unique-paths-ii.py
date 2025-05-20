#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
from typing import List
# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n_rows, n_cols = len(obstacleGrid), len(obstacleGrid[0])

        def recurse(r,c):
            # if there is grid=[[1]], then check if it is within bounds as well as 1
            if obstacleGrid[r][c] == 1 and 0<=r<n_rows and 0<=c<n_cols: return 0
            if r<0 or c<0: return 0
            if r==0 and c==0: return 1
            up = recurse(r-1,c)
            left = recurse(r,c-1)
            return up+left
        # return recurse(n_rows-1, n_cols-1)

        memo ={}
        def memoize(r,c):
            if (r,c) in memo: return memo[(r,c)]
            if obstacleGrid[r][c] == 1 and 0<=r<n_rows and 0<=c<n_cols: return 0
            if r<0 or c<0: return 0
            if r==0 and c==0: return 1
            memo[(r,c)] = memoize(r-1,c) + memoize(r,c-1)
            return memo[(r,c)]
        # return memoize(n_rows-1, n_cols-1)

        def tabulation():
            dp = [[-1]*n_cols for _ in range(n_rows)]

            for r in range(n_rows):
                for c in range(n_cols):
                    if obstacleGrid[r][c] == 1 and 0<=r<n_rows and 0<=c<n_cols: 
                        dp[r][c] = 0
                        continue
                    if r==0 and c==0: 
                        dp[r][c] = 1
                        continue

                    up, left = 0,0
                    if r>0: up = dp[r-1][c]
                    if c>0: left = dp[r][c-1]
                    dp[r][c] = up+left

            return dp[n_rows-1][n_cols-1]  
        # return tabulation()

        def iteration():
            prev = [0]*n_cols
            for r in range(n_rows):
                temp = [0]*n_cols
                for c in range(n_cols):
                    if obstacleGrid[r][c] == 1 and 0<=r<n_rows and 0<=c<n_cols:
                        temp[c] = 0
                        continue
                    if r==0 and c==0: 
                        temp[c] = 1
                        continue

                    up, left = 0,0
                    if r>0: up = prev[c]
                    if c>0: left = temp[c-1]
                    temp[c] = up+left
                prev = temp
            return prev[n_cols-1]
        return iteration()
    
# @lc code=end

# asked in  Amazon, Apple, Bloomberg, Facebook, GoDaddy, Goldman Sachs, Google, Mathworks, Microsoft, Snapchat