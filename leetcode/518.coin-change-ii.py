#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#
from typing import List
# @lc code=start
class Solution:
    ## return only the count so base case either returns a 1 or a 0
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        memo = {}
        def recurse_memo(idx,target):
            if (idx,target) in memo: return memo[(idx,target)]
            
            if idx == 0:
                # if condition satisfied return 1 else return 0
                return 1 if target%coins[idx] == 0 else 0
            
            not_picked = recurse_memo(idx-1, target)
            picked = 0
            if coins[idx]<=target:
                picked = recurse_memo(idx, target-coins[idx])
            memo[(idx,target)] = picked+not_picked
            return memo[(idx,target)]

        # return recurse_memo(n-1,amount)
    
        def tabulation():
            dp = [[0]*(amount+1) for _ in range(n)]
            for target in range(amount+1):
                if target%coins[0] == 0: dp[0][target] = 1

            for idx in range(1,n):
                for target in range(amount+1):
                    not_picked = dp[idx-1][target]
                    picked = 0
                    if coins[idx]<=target:
                        picked = dp[idx][target-coins[idx]]
                    dp[idx][target] = picked+not_picked

            return dp[n-1][amount]
        # return tabulation()
    
        def iteration():
            prev = [0]*(amount+1)
            for target in range(amount+1):
                if target%coins[0] == 0: prev[target] = 1

            for idx in range(1,n):
                temp = [0]*(amount+1)
                for target in range(amount+1):
                    not_picked = prev[target]
                    picked = 0
                    if coins[idx]<=target:
                        picked = temp[target-coins[idx]]
                    temp[target] = picked+not_picked
                prev = temp

            return prev[amount]
        # return iteration()
    
        def optimized():
            temp = [0]*(amount+1)
            for target in range(amount+1):
                if target%coins[0] == 0: temp[target] = 1

            for idx in range(1,n):
                for target in range(amount+1):
                    not_picked = temp[target]
                    picked = 0
                    if coins[idx]<=target:
                        picked = temp[target-coins[idx]]
                    temp[target] = picked+not_picked

            return temp[amount]
        return optimized()

# @lc code=end

# Amazon, Bloomberg, Facebook, Google, IXL, Microsoft, Oracle, Uber, Walmart Labs, Yahoo 