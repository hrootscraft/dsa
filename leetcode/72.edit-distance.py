#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

## we already know min. operations of 1. insertions and 2. deletions+insertions in s1 to convert to s2 would be len(s1)+len(s2)-len(longest_common_subsequence)
## here, we have a slight change, we are permitted deletions+insertions+replacement ie replace any character in s1 with any character
from functools import lru_cache

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int: # word1 -> word2
        n = len(word1)
        m = len(word2)  

        @lru_cache(maxsize=None)
        def recurse(idx1,idx2): # return the min # of operations to convert word1[0,idx1+1] to word2[0,idx2+1]
            # base case: 
            # 1. word1 gets exhausted when idx1==-1 ie we have an empty string & there's still part of word2 left to transform word1 to, then min. insert operations would be len(word2[0,idx2+1])
            if idx1 < 0: return idx2+1
            # 2. word2 gets exhausted, but there's still part of word1, then we need to delete that
            if idx2 < 0: return idx1+1

            if word2[idx2] == word1[idx1]: # chars match then we shrink the words and perform no operations
                return 0 + recurse(idx1-1,idx2-1)
            # else
            insert_op = 1 + recurse(idx1,idx2-1) # we insert word2[idx2] at the end of word1 and shrink word2 but keep word1 as is to match further
            delete_op = 1 + recurse(idx1-1,idx2) # delete the char in word1 and shrink it while keeping word2 as is
            replace_op = 1 + recurse(idx1-1,idx2-1) # replace the char in word1 so it matches that in word2 and shrink both words
            return min(insert_op,delete_op,replace_op)
        # return recurse(n-1,m-1)

        def tabulation():
            dp = [[0]*(m+1) for _ in range(n+1)]
            for idx1 in range(n+1): dp[idx1][0] = idx1 # on any row, the 0th column is the row no
            for idx2 in range(m+1): dp[0][idx2] = idx2 # on 0th row of all columns, the value is col itself

            for idx1 in range(1, n+1):
                for idx2 in range(1, m+1):
                    if word2[idx2-1] == word1[idx1-1]: 
                        dp[idx1][idx2] = dp[idx1-1][idx2-1]
                    else: 
                        dp[idx1][idx2] = 1 + min(dp[idx1-1][idx2-1], min(dp[idx1-1][idx2], dp[idx1][idx2-1]))

            return dp[n][m]
        # return tabulation()

        def iteration():
            prev = [0]*(m+1)
            # for idx1 in range(n+1): dp[idx1][0] = idx1 
            for idx2 in range(m+1): prev[idx2] = idx2

            for idx1 in range(1, n+1):
                temp = [0]*(m+1)
                temp[0] = idx1
                for idx2 in range(1, m+1):
                    if word2[idx2-1] == word1[idx1-1]: 
                        temp[idx2] = prev[idx2-1]
                    else: 
                        temp[idx2] = 1 + min(prev[idx2-1], min(prev[idx2], temp[idx2-1]))
                prev = temp
            return prev[m]
        return iteration()
# @lc code=end
