#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
# Adobe Amazon Bloomberg Coursera Cruise Automation Facebook 
# Goldman Sachs Google Microsoft Snapchat Twitter Two Sigma 
from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(p) # can be "ab*cd"
        m = len(s) # can be "abdefcd"

        # def isAllStars(idx):
        #     for i in range(idx+1):
        #         if p[i] != "*": return False
        #     return True

        # @lru_cache(maxsize=None)
        # def recurse(idx1,idx2):
        #     # base case has to return True or False
        #     if idx1<0 and idx2<0: return True # both strings got exhausted
        #     if idx1<0 and idx2>=0: return False # if string is exhausted but pattern is remaining
        #     if idx2<0 and idx1>=0: return isAllStars(idx1) # if pattern is exhausted but string is remaining, that string needs to be all "*" to return True
        
        #     if p[idx1] == s[idx2] or p[idx1] == "?":
        #         return recurse(idx1-1,idx2-1) 
        #     if p[idx1] == "*": # if the string has a * then either consider that as empty and reduce the string by 1 OR consider that * to match 1 char from pattern and reduce the pattern keeping the * as is in next iteration to match
        #         return recurse(idx1-1,idx2) or recurse(idx1,idx2-1) 
        #     return False # the characters cannot be matched
        # return recurse(n-1,m-1)

        def isAllStars_shifted(idx):
            for i in range(1, idx+1): # 1-based indexing
                if p[i-1] != "*": return False # 1 lesser
            return True

        # @lru_cache(maxsize=None)
        # def recurse_shifted(idx1,idx2):
        #     # base case has to return True or False
        #     if idx1 == 0 and idx2 == 0: return True # both strings got exhausted
        #     if idx1 == 0 and idx2 > 0: return False # if string is exhausted but pattern is remaining
        #     if idx2 == 0 and idx1 > 0: return isAllStars_shifted(idx1) # if pattern is exhausted but string is remaining, that string needs to be all "*" to return True
        
        #     if p[idx1-1] == s[idx2-1] or p[idx1-1] == "?":
        #         return recurse_shifted(idx1-1,idx2-1) 
        #     if p[idx1-1] == "*": # if the string has a * then either consider that as empty and reduce the string by 1 OR consider that * to match 1 char from pattern and reduce the pattern keeping the * as is in next iteration to match
        #         return recurse_shifted(idx1-1,idx2) or recurse_shifted(idx1,idx2-1) 
        #     return False # the characters cannot be matched
        # return recurse_shifted(n,m)
    
        def tabulation_shifted():
            dp = [[False]*(m+1) for _ in range(n+1)]
            dp[0][0] = True 
            # for idx2 in range(1,m+1): dp[0][idx2] = False # implicitly done in init above
            for idx1 in range(1,n+1): dp[idx1][0] = isAllStars_shifted(idx1)

            for idx1 in range(1,n+1):
                for idx2 in range(1,m+1):
                    if p[idx1-1] == s[idx2-1] or p[idx1-1] == "?":
                        dp[idx1][idx2] = dp[idx1-1][idx2-1]
                    elif p[idx1-1] == "*": 
                        dp[idx1][idx2] = dp[idx1-1][idx2] or dp[idx1][idx2-1] 
                    else: dp[idx1][idx2] = False
            return dp[n][m]
        # return tabulation_shifted()
    
        def iteration_shifted():
            prev = [False]*(m+1)
            prev[0] = True 
            # for idx2 in range(1,m+1): prev[idx2] = False # default init above

            # for idx1 in range(1,n+1): dp[idx1][0] = isAllStars_shifted(idx1) # handled below

            for idx1 in range(1,n+1):
                temp = [False]*(m+1)
                temp[0] = isAllStars_shifted(idx1)
                for idx2 in range(1,m+1):
                    if p[idx1-1] == s[idx2-1] or p[idx1-1] == "?":
                        temp[idx2] = prev[idx2-1]
                    elif p[idx1-1] == "*": 
                        temp[idx2] = prev[idx2] or temp[idx2-1] 
                    else: temp[idx2] = False
                prev = temp
            return prev[m]
        return iteration_shifted()
# @lc code=end

