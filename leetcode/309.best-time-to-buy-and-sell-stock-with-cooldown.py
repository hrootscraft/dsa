#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
from typing import List
from functools import cache
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def recurse(idx,canBuy):
            if idx>=n: return 0 # we might go above n when idx=n-1 so >=
            if canBuy:
                picked = -prices[idx] + recurse(idx+1,False)
                not_picked = 0 + recurse(idx+1,True)
                profit = max(picked,not_picked)
            if not canBuy: # sell
                picked = prices[idx] + recurse(idx+2,True) # you can buy only after a day after selling
                not_picked = 0 + recurse(idx+1,False) 
                profit = max(picked,not_picked)
            return profit
        # return recurse(0,True)

        def tabulation():
            dp = [[0]*2 for _ in range(n+2)]

            for idx in range(n-1,-1,-1):
                # for canBuy in range(2):
                #     if canBuy:
                #         profit = max(-prices[idx] + dp[idx+1][False],dp[idx+1][True])
                #     if not canBuy: # sell
                #         profit = max(prices[idx] + dp[idx+2][True],dp[idx+1][False]) # in space optimization we'll need a total of 3 1D arrays because we have idx+2 as well 
                #     dp[idx][canBuy] = profit
                dp[idx][True] = max(-prices[idx] + dp[idx+1][False],dp[idx+1][True])
                dp[idx][False] = max(prices[idx] + dp[idx+2][True],dp[idx+1][False])
            return dp[0][True]
        # return tabulation()
    
        def iteration():
            front1 = [0]*2 
            front2 = [0]*2 

            for idx in range(n-1,-1,-1):
                temp = [0]*2
                temp[True] = max(-prices[idx] + front1[False],front1[True])
                temp[False] = max(prices[idx] + front2[True],front1[False])

                # current/temp | front1 | front2
                front2 = front1
                front1 = temp

            return temp[True]
        return iteration()
# @lc code=end

# Amazon Apple Google 