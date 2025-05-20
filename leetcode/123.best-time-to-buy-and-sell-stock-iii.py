#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
from typing import List
from functools import lru_cache
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # cap = 2

        # @lru_cache(maxsize=None) # TC: O(n*2*3). SC: O(n*2*3)+O(n)
        # def recurse(idx,canBuy,cap): # TC: exponential. SC: auxiliary stack space
        #     if idx == n or cap == 0: return 0 # if reached the end of array or used up all transactions, return zero profit

        #     profit = 0
        #     if canBuy:
        #         picked = -prices[idx] + recurse(idx+1,False,cap)
        #         not_picked = 0 + recurse(idx+1,True,cap)
        #         profit = max(picked,not_picked)
        #     if not canBuy: # one transaction is complete only after selling and we have only 2 transactions' cap
        #         picked = prices[idx] + recurse(idx+1,True,cap-1)
        #         not_picked = 0 + recurse(idx+1,False,cap)
        #         profit = max(picked,not_picked)
        #     return profit
        # # return recurse(0,True,cap)

        # def tabulation(): # TC: O(n*2*3). SC: O(n*2*3)
        #     dp = [[[0]*(cap+1) for _ in range(2)] for _ in range(n+1)]

        #     # # base cases handled by default above
        #     # # when cap=0, idx and canBuy are variable
        #     # for idx in range(n+1):
        #     #     for canBuy in range(2):
        #     #         dp[idx][canBuy][0] = 0
        #     # # when idx=n, cap and canBuy are variable
        #     # for canBuy in range(2):
        #     #     for cap in range(3):
        #     #         dp[n][canBuy][cap] = 0

        #     for idx in range(n-1,-1,-1):
        #         for canBuy in range(2):
        #             for cp in range(1, cap+1):
        #                 profit = 0
        #                 if canBuy:
        #                     profit = max(-prices[idx] + dp[idx+1][False][cp],dp[idx+1][True][cp])
        #                 if not canBuy: 
        #                     profit = max(prices[idx] + dp[idx+1][True][cp-1],dp[idx+1][False][cp])
        #                 dp[idx][canBuy][cp] = profit
        #     return dp[0][True][cap]
        # # return tabulation()

        # def iteration(): # TC: O(n*2*3). SC: O(1)
        #     ahead = [[0]*(cap+1) for _ in range(2)]

        #     for idx in range(n-1,-1,-1):
        #         temp = [[0]*(cap+1) for _ in range(2)]
        #         for canBuy in range(2):
        #             for cp in range(1, cap+1):
        #                 profit = 0
        #                 if canBuy:
        #                     profit = max(-prices[idx] + ahead[False][cp],ahead[True][cp])
        #                 if not canBuy: 
        #                     profit = max(prices[idx] + ahead[True][cp-1],ahead[False][cp])
        #                 temp[canBuy][cp] = profit
        #         ahead = temp
        #     return ahead[True][cap]
        # # return iteration()
    
        # another approach would be to express the cap in terms of canBuy
        # ie you can have recurse(idx,transac_number) where transac_number 
        # is represented by BSBS ~ [0,1,2,3] buy (B) is even and sell is odd
        # why only BSBS and not BSBSBS because we have a cap of 2 transactions
        @lru_cache(maxsize=None)
        def recurse_(idx,transac_number):
            if idx==n or transac_number==4: return 0

            if transac_number%2==0: # when it's a buy
                profit = max(-prices[idx] + recurse_(idx+1,transac_number+1),recurse_(idx+1,transac_number))
            else: # when it's a sell
                profit = max(prices[idx] + recurse_(idx+1,transac_number+1),recurse_(idx+1,transac_number))
            return profit
        # return recurse_(0,0)
    
        def tabulation_():
            dp = [[0]*5 for _ in range(n+1)]
            # for idx in range(n+1): dp[idx][4] = 0
            # for tn in range(5): dp[n][tn] = 0

            for idx in range(n-1,-1,-1):
                for tn in range(3,-1,-1):
                    if tn%2==0: # when it's a buy
                        profit = max(-prices[idx] + dp[idx+1][tn+1],dp[idx+1][tn])
                    else: # when it's a sell
                        profit = max(prices[idx] + dp[idx+1][tn+1],dp[idx+1][tn])
                    dp[idx][tn] = profit
            return dp[0][0]
        # return tabulation_()
    
        def iteration_():
            ahead = [0]*5 
            # for idx in range(n+1): dp[idx][4] = 0
            # for tn in range(5): dp[n][tn] = 0

            for idx in range(n-1,-1,-1):
                temp = [0]*5
                for tn in range(3,-1,-1):
                    if tn%2==0: # when it's a buy
                        profit = max(-prices[idx] + ahead[tn+1],ahead[tn])
                    else: # when it's a sell
                        profit = max(prices[idx] + ahead[tn+1],ahead[tn])
                    temp[tn] = profit
                ahead = temp
            return ahead[0]
        return iteration_()
# @lc code=end
        
        
# Amazon Atlassian Bloomberg Citadel Facebook Flipkart Google Microsoft Rubrik Two Sigma 