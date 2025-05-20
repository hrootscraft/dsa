#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:    
    def longestPalindrome(self, s: str) -> str:
        ## DP - TC: O(n^2), SC: O(n^2)
        n = len(s)
        max_ = s[0]
        max_len = 1 # not needed in this problem

        if n==1: return max_
        
        # dp[i][j] repmaxents whether the substring from index i to 
        # index j (inclusive) is a palindrome
        dp = [[False]*n for _ in range(n)]

        # nested loops iterate over all possible lengths of substrings, 
        # starting from 1 up to the length of the string s. The inner 
        # loop iterates over all possible starting indices for substrings 
        # of the current length
        for curr_len in range(1, n+1):
            for idx in range(n-curr_len+1):
                if curr_len == 1:
                    dp[idx][idx] = True # all the diagonal elements with length 1 are palindromes
                    max_len = 1
                elif curr_len == 2:
                    dp[idx][idx+1] = (s[idx] == s[idx+1])
                    if dp[idx][idx+1]: # if the 2 consecutive characters match
                        max_len = 2
                        max_ = s[idx:idx+2] # update longest palindrome 
                else: # for substrings of length >= 3
                    # if first & last characters of the current substring are same AND ...
                    # to determine if the whole substring is a palindrome, we look at whether 
                    # the substring formed by excluding the first and last characters 
                    # (s[idx+1:idx+curr_len-1]) is itself a palindrome. we look up this information 
                    # in dp[i+1][i+curr_len-2]. this is a recursive check.
                    dp[idx][idx+curr_len-1] = ((s[idx] == s[idx+curr_len-1]) and dp[idx+1][idx+curr_len-2])
                    # if both conditions are true, ie, the first and last characters match 
                    # and the substring without these characters is a palindrome, then we 
                    # update dp[i][i+curr_len-1] to True, indicating that the current substring is a palindrome
                    if dp[idx][idx+curr_len-1]:
                        max_ = s[idx:idx+curr_len]
                        max_len = curr_len
        return max_
    
        ## TWO POINTER - TC: O(n^2), SC: O(1)
        # max_ = ""
        # max_len = 0
        # n = len(s)

        # def check_update_palindrome(l_ptr, r_ptr):
        #     nonlocal max_, max_len
        #     while l_ptr >= 0 and r_ptr < n and s[l_ptr]==s[r_ptr]: # while the string is a palindrome and the pointers are within bounds
        #         if (r_ptr-l_ptr+1) > max_len: # if the found palindrome greater than previous, update
        #             max_len = r_ptr-l_ptr+1
        #             max_ = s[l_ptr:r_ptr+1]
        #         l_ptr -= 1
        #         r_ptr += 1

        # for idx in range(n):
        #     check_update_palindrome(idx, idx) # odd length
        #     check_update_palindrome(idx, idx+1) # even length
            
        # return max_         
# @lc code=end

# Adobe Airbnb Alibaba Amazon Apple Baidu Bloomberg Cisco eBay Facebook GoDaddy
# Google Huawei caMorgan Mathworks Microsoft Oracle Pure Storage Roblox 
# Samsung SAP ServiceNow Tencent Uber VMware Walmart Labs Wayfair Yahoo Yandex

## APR1: generate all substrings - O(n^2) and then check if it is a palindrome - O(n) so TC here is O(n^3)
## APR2: for every character in the string consider that character as a middle character and expand outwards 
# (check if adjacent elements on both sides are same) this works if the palindromic string is odd in length
# for even length strings we consider current & next character as the centre & expand around it. TC: O(n^2)