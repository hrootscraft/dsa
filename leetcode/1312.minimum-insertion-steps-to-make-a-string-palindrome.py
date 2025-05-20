#
# @lc app=leetcode id=1312 lang=python3
#
# [1312] Minimum Insertion Steps to Make a String Palindrome
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        def longestCommonSubsequence(text1: str, text2: str) -> int:
            n = len(text1)
            m = len(text2)

            def iteration_shifted():
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
    
        lps = longestCommonSubsequence(s,s[::-1]) # find lcs of string and its reverse
        return n-lps
# @lc code=end

# Approach:
# 1. keep the palindromic SUBSEQUENCE (NOT substring) in s intact
# 2. if we're trying to minimize the no.of insertions, we'll keep 
# the longest palindromic SUBSEQUENCE in s intact. 
# 3. now, what we do is copy the remaining characters from s at appropriate places
# to get a palindrome. basically, the min. no.of insertions is 
# len(s)-len(longest palindromic subsequence). refer 516 leetcode.