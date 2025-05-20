#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
# Adobe, Alibaba, Amazon, Apple, Bloomberg, Facebook, Goldman Sachs, Google, 
# Mathworks, Microsoft, Oracle, Snapchat, Uber, VMware, Walmart Labs 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # the following function gives the number of unique ways to reach 0,0 from r,c
        def recurse(r,c): # top down approach
            if r==0 and c==0: return 1 # you reached 0,0
            if r<0 or c<0: return 0 # you reach out of bounds so don't count that path
            # since the robot can move only down or right, in our top down approach we can make it up or left
            up = recurse(r-1,c)
            left = recurse(r,c-1)
            return up+left
        # return recurse(m-1,n-1) # TC: O(2^(m*n)) - for every box we explore two directions; SC: stack space is the path length i.e. O(m-1 + n-1)

        memo = {}
        def memoize(r,c):
            if (r,c) in memo: return memo[(r,c)]

            if r==0 and c==0: return 1
            if r<0 or c<0: return 0

            up = memoize(r-1,c)
            left = memoize(r,c-1)

            memo[(r,c)] = up+left
            return memo[(r,c)]
        
        # return memoize(m-1,n-1) # TC: is no more exponential, at max the # of calls will be m*n so O(m*n); SC: O(m-1 + n-1) + O(m*n)

        dp = [[-1]*n for _ in range(m)]
        def tabulation(): # bottom up approach
            dp[0][0] = 1 # no.of unique paths to reach 0,0 is 1 from 0,0
            for r in range(m):
                for c in range(n):
                    if r==0 and c==0: continue
                    up, left = 0, 0 # init variables to store number of ways from above and from the left
                    if r>0: up = dp[r-1][c]
                    if c>0: left = dp[r][c-1]
                    dp[r][c] = up+left
            return dp[m-1][n-1]    

        # return tabulation() # TC: O(m*n) - two nested loops, SC: O(m*n) - external grid

        def iteration():
            prev = [0]*n # create a prev row initially whose values will be used to calculate up and the current row will be used for left
            # prev      0 0 0 0
            # current   1 . . . # 1 because at (0,0) you have 1 unique path to reach (0,0)
            # in the next iteration the current will increase by 1 in row and prev row will be reassigned to current row
            for r in range(m):
                temp = [0]*n # temporary row to store current row results
                for c in range(n):
                    if r==0 and c==0: # base case: if we are at the top-left corner, there is one way to reach it
                        temp[c] = 1
                        continue
                    up = 0
                    left = 0 
                    if r>0: up = prev[c] # if moving up is a valid option
                    if c>0: left = temp[c-1] # if moving left is a valid option
                    temp[c] = up+left
                prev = temp
            return prev[n-1] # last element in the previous row now contains the total number of ways to reach the destination
        # return iteration() # TC: O(m*n) - two nested loops, SC: O(n) - external array of size n
    
        def combinatorial_sol(): # https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/
            path = 1
            # calculate (m+n-2)CHOOSE(n-1) which will be (m+n-2)! / (n-1)! (m-1)!
            for i in range(n, (m+n-1)):
                path *= i
                path //= (i-n+1)
            return path
        return combinatorial_sol() # TC: O(M), M is the maximum of m and n; SC: O(1)

# @lc code=end

# how do you go from recursion to tabulation?
# 1. declare base case
# 2. express all states in for loop
# 3. copy the recursion snippet
    
# heuristic approach:

# def numberOfPaths(m, n):
#     dp = [[0]*n for _ in range(m)]
#     for i in range(m): dp[i][0] = 1 # init first col with 1
#     for j in range(n): dp[0][j] = 1 # init first row with 1
 
#     # calculate count of paths for other cells in bottom-up manner using the recursive solution
#     for i in range(1, m):
#         for j in range(1, n):
#             dp[i][j] = dp[i-1][j] + dp[i][j-1]
#     return dp[m-1][n-1]
