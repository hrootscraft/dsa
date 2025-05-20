#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

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
    
        return longestCommonSubsequence(s,s[::-1]) # find lcs of string and its reverse
# @lc code=end

## refer 1143 for explanation of lcs

#  Amazon, Apple, Bloomberg, Facebook, LinkedIn, Microsoft, Uber 
## approach 1 - brute force: generate all subsequences, check if 
# any of them is a palindrome and then return the longest length
## approach 2 - if the original string is reversed then we can find 
# lcs of those two strings which is nothing but a palindrome 