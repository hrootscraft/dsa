# weight = [2,4,6] | value = [5,11,13] | W = 10
# If this was knapsack problem, then we'd use only instance of weight 
# but in this problem of unbounded knapsack we have infinite supply of 
# denominations/weights each of whose value is given by the value array
# similar to coin change leetcode

# problem statement: A thief wants to rob a store. He is carrying a bag of 
# capacity W. The store has ‘n’ items of infinite supply. Its weight is given 
# by the ‘weight’ array and its value by the ‘value’ array. He can either include an 
# item in its knapsack or exclude it but can’t partially have it as a fraction. 
# We need to find the maximum value of items that the thief can steal. He can 
# take a single item any number of times he wants and put it in his knapsack.

from functools import lru_cache

weight = [2,4,6] 
value = [5,11,13] 
W = 10

def solve(weight, value, W):
    n = len(weight)

    @lru_cache(maxsize=None)
    def recurse(idx, curr_weight): # returns maximum value of idx+1 items in the bag of capacity curr_weight
        if idx==0: # when there are no more items to consider
            # if weight[0]<=curr_weight:
            #     return value[0]
            # return float("-inf")

            # we can also write this as but technically above one is better
            return (curr_weight//weight[0])*value[0]
        
        not_picked = 0 + recurse(idx-1,curr_weight)
        picked = float("-inf")
        if weight[idx]<=curr_weight:
            picked = value[idx] + recurse(idx,curr_weight-weight[idx])
        return max(picked,not_picked)
        
    # return recurse(n-1,W) # get the maximum value of n items in the bag of capacity W

    def tabulation():
        dp = [[0]*(W+1) for _ in range(n)]
        for curr_weight in range(W+1):
            dp[0][curr_weight] = (curr_weight//weight[0])*value[0]

        for idx in range(1,n):
            for curr_weight in range(W+1):
                not_picked = 0 + dp[idx-1][curr_weight]
                picked = float("-inf")
                if weight[idx]<=curr_weight:
                    picked = value[idx] + dp[idx][curr_weight-weight[idx]]
                dp[idx][curr_weight] = max(picked,not_picked)

        return dp[n-1][W]
    # return tabulation()

    def iteration():
        prev = [0]*(W+1)
        for curr_weight in range(W+1):
            prev[curr_weight] = (curr_weight//weight[0])*value[0]

        for idx in range(1,n):
            temp = [0]*(W+1)
            for curr_weight in range(W+1):
                not_picked = 0 + prev[curr_weight]
                picked = float("-inf")
                if weight[idx]<=curr_weight:
                    picked = value[idx] + temp[curr_weight-weight[idx]]
                temp[curr_weight] = max(picked,not_picked)
            prev = temp

        return prev[W]
    # return iteration()

    def further_space_optimized(): 
        # from 2 arrays of 1x(W+1) we can use 1 array of 1x(W+1) because 
        # when computing the temp aka current element we only require 
        # previous array's one value i.e the same as the current column (curr_weight)
        # and the elements in the current row's (aka temp) element which are on the 
        # left of curr_weight because temp[curr_weight-weight[idx]
        # so what we can do is use only temp ie the current array and update the same column element
        temp = [0]*(W+1)
        for curr_weight in range(W+1):
            temp[curr_weight] = (curr_weight//weight[0])*value[0]

        for idx in range(1,n):
            for curr_weight in range(W+1):
                not_picked = 0 + temp[curr_weight]
                picked = float("-inf")
                if weight[idx]<=curr_weight:
                    picked = value[idx] + temp[curr_weight-weight[idx]]
                temp[curr_weight] = max(picked,not_picked)
        return temp[W]
    return further_space_optimized()

print(solve(weight, value, W)) # 27