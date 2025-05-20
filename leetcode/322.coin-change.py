#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
from typing import List
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # greedy approach when in the sorted denominations array the sum of first two deno. 
        # # does not exceed the third one's value ie there is some sort of uniformity
        # count = 0
        # sorted_coins = sorted(coins)
        # idx = len(sorted_coins)-1
        # while idx>=0 and amount!=0:
        #     if amount//sorted_coins[idx] == 0: idx -= 1 # if the denomination is greater than the amount then skip it and go on to the smaller denomination
        #     else:
        #         count += amount//sorted_coins[idx]
        #         amount = amount%sorted_coins[idx]
        #         idx -= 1

        # if amount != 0: return -1
        # else: return count

        # but we know that denominations in this problem do not satisfy any such condition
        # hence, we have to use recursion/dp to try out every possible combination
        ## similar to knapsack problem
        n = len(coins)
        MAX_VALUE = 10**6

        memo = {}
        def recurse_memo(idx, target):
            if (idx,target) in memo: return memo[(idx,target)]
            if idx == 0:
                if target%coins[idx] == 0: 
                    memo[(idx,target)] = target//coins[idx]
                    return memo[(idx,target)] 
                else: 
                    memo[(idx,target)] = MAX_VALUE
                    return memo[(idx,target)] 

            not_picked = 0 + recurse_memo(idx-1,target)
            picked = MAX_VALUE
            if coins[idx]<=target:
                picked = 1 + recurse_memo(idx,target-coins[idx])

            memo[(idx,target)] = min(picked, not_picked)
            return memo[(idx,target)]
        
        # res = recurse_memo(n-1, amount) # TC: >>O(2^n) SC: >>O(n)
        # return res if res != MAX_VALUE else -1 # returns the min no.of coins amounting to amount
    
        def tabulation():
            dp = [[0]*(amount+1) for _ in range(n)]
            for amt in range(amount+1):
                if amt%coins[0] == 0:
                    dp[0][amt] = amt//coins[0]
                else: dp[0][amt] = MAX_VALUE

            for idx in range(1,n):
                for amt in range(amount+1):
                    not_picked = 0 + dp[idx-1][amt]
                    picked = MAX_VALUE
                    if coins[idx]<=amt:
                        picked = 1 + dp[idx][amt-coins[idx]]
                    dp[idx][amt] = min(picked, not_picked)

            return dp[n-1][amount]

        # res = tabulation() # TC: O(n*amount) SC: O(n*amount)+O(n)
        # return res if res != MAX_VALUE else -1

        def iteration():
            prev = [0]*(amount+1)
            for amt in range(amount+1):
                if amt%coins[0] == 0:
                    prev[amt] = amt//coins[0]
                else: prev[amt] = MAX_VALUE

            for idx in range(1,n):
                temp = [0]*(amount+1)
                for amt in range(amount+1):
                    not_picked = 0 + prev[amt]
                    picked = MAX_VALUE
                    if coins[idx]<=amt:
                        picked = 1 + temp[amt-coins[idx]]
                    temp[amt] = min(picked, not_picked)
                prev = temp

            return prev[amount]
        
        res = iteration() # TC: O(n*amount) SC: O(amount), two external arrays of size ‘amount+1’.
        return res if res != MAX_VALUE else -1

# @lc code=end

# Adobe, Affirm, Airbnb, Amazon, Apple, BlackRock, Bloomberg, Capital One,
# Facebook, Goldman Sachs, Google, caMorgan, LinkedIn, Microsoft, Oracle, 
# Uber, Visa, VMware, Walmart Labs, Yahoo, Zappos