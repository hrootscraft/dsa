#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
# @lc code=start
from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        @lru_cache(maxsize=None)
        def recurse(idx1,idx2): ## TC: O(n*m)-n*m states therefore at max ‘n*m’ new problems will be solved; SC:  O(n*m) + O(n+m) - n*m values cached (2D array), auxiliary recursion stack space(O(N+M))
            # base case
            if idx1 < 0 or idx2 < 0: # negative indices ~ end of string
                return 0 

            # when matched, add 1
            if text1[idx1] == text2[idx2]:
                return 1+recurse(idx1-1,idx2-1)
            # when unmatched move in both directions
            # return 0+max(recurse(idx1-1,idx2),recurse(idx1,idx2-1))
            return max(recurse(idx1-1,idx2),recurse(idx1,idx2-1))
        # return recurse(n-1,m-1) # returns lcs of string1[0 to n-1] and string2[0 to m-1]

        # for base case we see that recursive calls go to negative indices but we cannot access dp[-1] so we do shifting of indices
        # now instead of calling (n-1,m-1) we call (n,m) but it means the former; basically (0,1) means (-1,0) ie we shift by 1 index
        # and so the recursive function might as well be:
        @lru_cache(maxsize=None)
        def recurse_shifted(idx1,idx2):
            if idx1==0 or idx2==0: # ~ idx==-1
                return 0
            if text1[idx1-1] == text2[idx2-1]: # everything remains same except string comparison indices are shifted
                return 1+recurse_shifted(idx1-1,idx2-1)
            return max(recurse_shifted(idx1-1,idx2),recurse_shifted(idx1,idx2-1))
        # return recurse_shifted(n,m)

        def tabulation_shifted(): ## TC: O(n*m) two nested loops, SC: O(n*m) for dp grid, stack space is eliminated
            dp = [[-1]*(m+1) for _ in range(n+1)]
            for idx1 in range(n+1): dp[idx1][0] = 0
            for idx2 in range(m+1): dp[0][idx2] = 0

            for idx1 in range(1,n+1):
                for idx2 in range(1,m+1):
                    if text1[idx1-1] == text2[idx2-1]: 
                        dp[idx1][idx2] = 1+dp[idx1-1][idx2-1]
                    else:
                        dp[idx1][idx2] = max(dp[idx1-1][idx2],dp[idx1][idx2-1])

            return dp[n][m]    
        # return tabulation_shifted()

        def iteration_shifted(): ## TC: O(n*m) two nested loops, SC: O(m) for arrays
            prev = [0]*(m+1)
            for idx1 in range(1,n+1):
                temp = [0]*(m+1)
                for idx2 in range(1,m+1):
                    if text1[idx1-1] == text2[idx2-1]: 
                        temp[idx2] = 1+prev[idx2-1]
                    else:
                        temp[idx2] = max(prev[idx2],temp[idx2-1])
                prev = temp
            return prev[m]    
        return iteration_shifted()

# @lc code=end

#  Amazon, Google, Microsoft 

## For plain recursion, TC: 2^n * 2^m ~ exponential, we cache it then