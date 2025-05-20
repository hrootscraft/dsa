#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
from typing import List
from functools import lru_cache
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n==0: return 0 # no stocks, zero profit
        
        ## without caching : TC: O(2^n) ... n->no.of days. For each day there's 2 choices to buy or not buy. SC: O(n) auxiliary stack space
        ## with caching : TC: O(n*2) complexity reduced to unique subproblems which is proportional to # of distinct states which are at max 2*n. SC: recursion stack space O(n) and cache space O(n*2) 
        @lru_cache(maxsize=None)
        def recurse(idx, canBuy): # returns max profit that can be made in idx+1 days
            if idx==n: # when we are done trading on all given days, there is no money to transact & and so we cannot add/subtract from the profit
                return 0
            
            profit = 0
            if canBuy:
                # picked = -prices[idx] + recurse(idx+1,False) # when you buy you deduct from your profit so -prices[idx] (ASSUME THE PROFIT IS WITH YOU)
                # not_picked = 0 + recurse(idx+1,True) # no transaction
                # profit = max(picked,not_picked)
                profit = max(-prices[idx] + recurse(idx+1,False), recurse(idx+1,True))
            elif not canBuy: # when you cannot buy, you can sell
                # picked = prices[idx] + recurse(idx+1,True) # when you sell you add to the profit so +prices[idx]
                # not_picked = 0 + recurse(idx+1,False) # no transaction but still carry forward the flag of cannot buy because you've bought before
                # profit = max(picked,not_picked) 
                profit = max(prices[idx] + recurse(idx+1,True), recurse(idx+1,False))
            return profit
        # return recurse(0,True) # give complete liberty to buy 0th index and get me the max profit on day 0

        ## TC: O(n*2) two nested loops. SC: external grid of size n*2 (stack space eliminated)
        def tabulation():
            dp = [[0]*2 for _ in range(n+1)] # canBuy signifies two variables: picked/bought and not_picked/not bought
            # dp[n][0] = dp[n][1] = 0 # no more days to trade and so max profit is 0 # handled by default above

            for idx in range(n-1,-1,-1): # idx goes from n-1 to 0
                for canBuy in range(2):
                    profit = 0
                    if canBuy:
                        profit = max(-prices[idx] + dp[idx+1][False], dp[idx+1][True])
                    elif not canBuy: 
                        profit = max(prices[idx] + dp[idx+1][True], dp[idx+1][False])
                    dp[idx][canBuy] = profit
            
            return dp[0][1] 
        # return tabulation()

        ## TC: O(n*2) two nested loops. SC: O(1)
        def iteration():
            ahead = [0]*2 # ahead[0] signifies profit after not picked and ahead[1] signifies profit after picked
            ahead[0] = ahead[1] = 0 # we start from n-1 so this is the one at nth 

            for idx in range(n-1,-1,-1):
                temp = [0]*2 # stores the current 
                for canBuy in range(2):
                    profit = 0
                    if canBuy:
                        profit = max(-prices[idx] + ahead[False], ahead[True])
                    elif not canBuy: 
                        profit = max(prices[idx] + ahead[True], ahead[False])
                    temp[canBuy] = profit
                ahead = temp     

            return ahead[1] 
        # return iteration()

        ## TC: O(n*2) two nested loops. SC: O(1)
        def using_variables():
            ahead_not_picked = ahead_picked = 0

            for idx in range(n-1,-1,-1):
                temp_not_picked = temp_picked = 0
                for canBuy in range(2):
                    if canBuy:
                        temp_picked = max(-prices[idx] + ahead_not_picked, ahead_picked)
                    elif not canBuy: 
                        temp_not_picked = max(prices[idx] + ahead_picked, ahead_not_picked)

                ahead_not_picked = temp_not_picked
                ahead_picked = temp_picked
            return ahead_picked
        # return using_variables()

        ## TC: O(n) two nested loops. SC: O(1)
        def optimized():
            ahead_not_picked = ahead_picked = 0

            for idx in range(n-1,-1,-1):
                temp_picked = max(-prices[idx] + ahead_not_picked, ahead_picked)
                temp_not_picked = max(prices[idx] + ahead_picked, ahead_not_picked)

                ahead_not_picked = temp_not_picked
                ahead_picked = temp_picked

            return ahead_picked
        return optimized()
# @lc code=end

# Adobe Alibaba Amazon Apple Bloomberg Citadel Facebook 
# Goldman Sachs Google Microsoft Oracle Uber Yahoo