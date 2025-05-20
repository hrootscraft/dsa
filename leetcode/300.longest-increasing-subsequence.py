#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
from typing import List
import functools
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @functools.lru_cache(None)
        def recurse(curr_idx,prev_idx): # prev will allow us to know whether the current element is greater than it and can be included in the subsequence
            if curr_idx == n: 
                return 0

            not_picked = 0 + recurse(curr_idx+1,prev_idx)
            picked = 0
            if prev_idx==-1 or nums[curr_idx]>nums[prev_idx]:
                picked = 1 + recurse(curr_idx+1,curr_idx)
            return max(picked,not_picked)

        # return recurse(0,-1) # returns the LIS in array[0:] when prev_idx included was -1 

        def tabulation():
            # curr_idx goes from 0 to n-1 while prev_idx goes from -1 to n-1
            # so to store -1 we shift it by 1 to the right ie -1~0, 0~1, 1~2, ...
            # so now prev_idx goes from 0 to n
            dp = [[0]*(n+1) for _ in range(n+1)]
            for prev_idx in range(n+1): dp[n][prev_idx] = 0

            for curr_idx in range(n-1,-1,-1):
                for prev_idx in range(n,-1,-1):
                    not_picked = 0 + dp[curr_idx+1][prev_idx]
                    picked = 0
                    if prev_idx==0 or nums[curr_idx]>nums[prev_idx-1]: # adjust prev_idx
                        picked = 1 + dp[curr_idx+1][curr_idx+1] # adjust prev_idx
                    dp[curr_idx][prev_idx] = max(picked,not_picked)
            
            return dp[0][0]
        # return tabulation()

        def iteration():
            ahead = [0]*(n+1)
            # for prev_idx in range(n+1): ahead[prev_idx] = 0

            for curr_idx in range(n-1,-1,-1):
                temp = [0]*(n+1)
                for prev_idx in range(n,-1,-1):
                    not_picked = 0 + ahead[prev_idx]
                    picked = 0
                    if prev_idx==0 or nums[curr_idx]>nums[prev_idx-1]: # adjust prev_idx
                        picked = 1 + ahead[curr_idx+1] # adjust prev_idx
                    temp[prev_idx] = max(picked,not_picked)
                ahead = temp

            return ahead[0]
        return iteration()
    
# @lc code=end

# Adobe Amazon Apple Atlassian Facebook Google Microsoft Oracle Salesforce Uber Visa VMware 