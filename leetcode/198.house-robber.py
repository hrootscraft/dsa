#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
from typing import List
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def recurse(idx): # this funct signifies the maximum sum of the subsequence from [0,idx]
            if idx == 0: return nums[idx] # if 0 is reached that means 1 was not picked, so we pick the element at 0
            if idx < 0: return 0 # if 1 is picked then idx becomes -ve, in that case we do not add anything to the sum
            picked = nums[idx] + recurse(idx-2) # since adjacent elements cannot be picked, we jump to idx-2 and not idx-1
            not_picked = 0 + recurse(idx-1)
            return max(picked, not_picked) 
        
        def memoize(idx):
            if idx in memo: return memo[idx]
            if idx == 0: return nums[idx]
            if idx < 0: return 0
            picked = nums[idx] + memoize(idx-2)
            not_picked = 0 + memoize(idx-1)
            memo[idx] = max(picked, not_picked) 
            return memo[idx]
        
        def tabulation():
            dp = [-1]*(n) # we can use negative numbers because by given conditions, array elements are all positive and the sum won't become negative
            dp[0] = nums[0] 
            for i in range(1,n):
                # picked = nums[i] + tabulation(i-2)
                picked = nums[i]
                if i>1: # if there are at least two elements before the current element
                    picked += dp[i-2]
                not_picked = 0 + dp[i-1]
                dp[i] = max(picked, not_picked) 
            return dp[n-1]
        
        def iteration():
            prev = nums[0] # first element
            second_to_prev = 0 # there is no element before the first

            for i in range(1,n):
                picked = nums[i]
                if i>1: picked += second_to_prev
                not_picked = 0 + prev
                curr_i = max(picked, not_picked) 
                second_to_prev = prev
                prev = curr_i
            return prev
        
        # return recurse(len(nums)-1)
        # return memoize(n-1)
        # return tabulation()
        return iteration()
# @lc code=end

