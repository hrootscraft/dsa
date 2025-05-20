#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        def iteration_shifted(): ## TC: O(n*m) two nested loops, SC: O(m) for arrays
            prev = [0]*(m+1)
            for idx1 in range(1,n+1):
                temp = [0]*(m+1)
                for idx2 in range(1,m+1):
                    if word1[idx1-1] == word2[idx2-1]: 
                        temp[idx2] = 1+prev[idx2-1]
                    else:
                        temp[idx2] = max(prev[idx2],temp[idx2-1])
                prev = temp
            return prev[m]    

        lcs = iteration_shifted()
        return n+m-2*lcs
# @lc code=end
# refer 1143 for lcs