#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Common Supersequence 
#

## refer /home/rutuja/dsa-python/dp/longest_common_subsequence.py

# @lc code=start
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        def tabulation_shifted(): # dp table from lcs 
            dp = [[-1]*(m+1) for _ in range(n+1)]
            for idx1 in range(n+1): dp[idx1][0] = 0
            for idx2 in range(m+1): dp[0][idx2] = 0

            for idx1 in range(1,n+1):
                for idx2 in range(1,m+1):
                    if str1[idx1-1] == str2[idx2-1]: dp[idx1][idx2] = 1+dp[idx1-1][idx2-1]
                    else: dp[idx1][idx2] = max(dp[idx1-1][idx2],dp[idx1][idx2-1])
            return dp
    
        dp = tabulation_shifted()
        len_lcs = dp[n][m]
        ans = "$"*(n+m-len_lcs) # the shortest common supersequence is of length n+m-len_lcs
        idx1 = n
        idx2 = m

        while idx1>0 and idx2>0:
            if str1[idx1-1] == str2[idx2-1]:
                ans = str1[idx1-1] + ans[:-1]
                idx1 -= 1
                idx2 -= 1
            elif dp[idx1-1][idx2] > dp[idx1][idx2-1]:
                ans = str1[idx1-1] + ans[:-1] # difference b/w printing lcs
                idx1 -= 1
            else:
                ans = str2[idx2-1] + ans[:-1] # difference b/w printing lcs
                idx2 -= 1
        
        # add remaing characters - only one of the below two while loops will run 
        while idx1 > 0:
            ans = str1[idx1-1] + ans[:-1]
            idx1 -= 1
        while idx2 > 0:
            ans = str2[idx2-1] + ans[:-1]
            idx2 -= 1

        return ans
# @lc code=end