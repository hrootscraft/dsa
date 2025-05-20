#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ## brute force: generate all subsequences & check if it matches t, (TLE)
        # n = len(s)
        # number_of_subsequences = 1<<n
        # res = 0
        # for num in range(number_of_subsequences):
        #     subseq = ""
        #     for i in range(n):
        #         if num & 1<<i > 0: subseq += s[i]
        #     if subseq == t: res += 1
        # return res

        n = len(s)
        m = len(t)
        @lru_cache(maxsize=None) 
        def recurse(idx1,idx2): # idx1 keeps track of s1 and idx2 of s2
            if idx2<0: # when string2 is exhausted, we have a match
                return 1
            if idx1<0: # when string1 is exhausted and string2 is still remaining, we did not find a match
                return 0
            
            if s[idx1] == t[idx2]:
                picked = recurse(idx1-1,idx2-1)
                not_picked = recurse(idx1-1,idx2)
                return picked+not_picked
            else:
                return recurse(idx1-1,idx2)
        # return recurse(n-1,m-1)

        def recurse_shifted(idx1,idx2): # for shifted recursion refer LCS 1143 leetcode
            if idx2 == 0: return 1
            if idx1 == 0: return 0

            if s[idx1-1] == t[idx2-1]:
                picked = recurse_shifted(idx1-1,idx2-1)
                not_picked = recurse_shifted(idx1-1,idx2)
                return picked+not_picked
            else:
                return recurse_shifted(idx1-1,idx2)
        # return recurse_shifted(n,m)

        def tabulation_shifted(): 
            dp = [[0]*(m+1) for _ in range(n+1)]
            for idx1 in range(n+1): dp[idx1][0] = 1
            # for idx2 in range(m+1): dp[0][idx2] = 0

            for idx1 in range(1,n+1):
                for idx2 in range(1,m+1):
                    if s[idx1-1] == t[idx2-1]: 
                        dp[idx1][idx2] = dp[idx1-1][idx2-1] + dp[idx1-1][idx2]
                    else:
                        dp[idx1][idx2] = dp[idx1-1][idx2]
            return dp[n][m]
        # return tabulation_shifted()
    
        def iteration_shifted():
            prev = [0]*(m+1)
            prev[0] = 1

            for idx1 in range(1,n+1):
                temp = [0]*(m+1)
                temp[0] = 1
                for idx2 in range(1,m+1):
                    if s[idx1-1] == t[idx2-1]: 
                        temp[idx2] = prev[idx2-1] + prev[idx2]
                    else:
                        temp[idx2] = prev[idx2]
                prev = temp
            return prev[m]
        # return iteration_shifted()

        def space_optimized():
            # we're using only previous to compute current aka temp
            # so we can optimize it to use only 1 temp array 
            # refer knapsack 1D array optimization: /home/rutuja/dsa-python/dp/01knapsack.py
            prev = [0]*(m+1)
            prev[0] = 1
            for idx1 in range(1, n+1):
                for idx2 in range(m, 0, -1): # go from m to 1 
                    if s[idx1-1] == t[idx2-1]: 
                        prev[idx2] = prev[idx2-1] + prev[idx2]
                    else:
                        prev[idx2] = prev[idx2]
            return prev[m]
        return space_optimized()
# @lc code=end

# Amazon Barclays Google 

## RECURSION - 
# TC: O((2^n)*(2^m)) ~ exponential, 2^n subsequences of s and 2^m of t and we match them; 
# SC: O(n+m) auxiliary stack space assuming parallel comparisons

## MEMOIZED RECURSION - 
# TC: O(n*m) :new states calculated 
# SC: O(n*m) + O(n+m) :dp grid ie storage of states and auxiliary stack space

## TABULATION -
# TC: O(n*m) 2 nested loops
# SC: O(n*m) dp grid

## ITERATION -
# TC: O(n*m) 2 nested loops
# SC: O(m) 2 1D arrays

## SPACE OPTIMIZED -
# TC: O(n*m) 2 nested loops
# SC: O(m) 1 1D array