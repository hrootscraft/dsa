#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#
from typing import List
from functools import cache

# @lc code=start
class Solution: # refer leetcode 122
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        @cache
        def recurse(idx,canBuy):
            if idx==n: return 0 
            profit = 0
            if canBuy:
                picked = -prices[idx] + recurse(idx+1,False)
                not_picked = 0 + recurse(idx+1,True)
                profit = max(picked,not_picked)
            if not canBuy: # sell
                picked = prices[idx]-fee + recurse(idx+1,True) # after a transaction of BS (buy-sell), a transaction fee is charged so take that out from our profit
                not_picked = 0 + recurse(idx+1,False) 
                profit = max(picked,not_picked)
            return profit
        # return recurse(0,True)

        def tabulation():
            dp = [[0]*2 for _ in range(n+1)] 

            for idx in range(n-1,-1,-1): 
                for canBuy in range(2):
                    profit = 0
                    if canBuy:
                        profit = max(-prices[idx] + dp[idx+1][False], dp[idx+1][True])
                    elif not canBuy: 
                        profit = max(prices[idx]-fee + dp[idx+1][True], dp[idx+1][False])
                    dp[idx][canBuy] = profit
            
            return dp[0][1] 
        # return tabulation()

        def iteration():
            ahead = [0]*2 
            ahead[0] = ahead[1] = 0 

            for idx in range(n-1,-1,-1):
                temp = [0]*2 # stores the current 
                for canBuy in range(2):
                    profit = 0
                    if canBuy:
                        profit = max(-prices[idx] + ahead[False], ahead[True])
                    elif not canBuy: 
                        profit = max(prices[idx]-fee + ahead[True], ahead[False])
                    temp[canBuy] = profit
                ahead = temp     

            return ahead[1] 
        # return iteration()

        def using_variables():
            ahead_not_picked = ahead_picked = 0

            for idx in range(n-1,-1,-1):
                temp_not_picked = temp_picked = 0
                for canBuy in range(2):
                    if canBuy:
                        temp_picked = max(-prices[idx] + ahead_not_picked, ahead_picked)
                    elif not canBuy: 
                        temp_not_picked = max(prices[idx]-fee + ahead_picked, ahead_not_picked)

                ahead_not_picked = temp_not_picked
                ahead_picked = temp_picked
            return ahead_picked
        # return using_variables()

        def optimized():
            ahead_not_picked = ahead_picked = 0

            for idx in range(n-1,-1,-1):
                temp_picked = max(-prices[idx] + ahead_not_picked, ahead_picked)
                temp_not_picked = max(prices[idx]-fee + ahead_picked, ahead_not_picked)

                ahead_not_picked = temp_not_picked
                ahead_picked = temp_picked

            return ahead_picked
        return optimized()
# @lc code=end

# Bloomberg Facebook Google 