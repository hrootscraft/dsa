# Problem statement
# A thief is robbing a store and can carry a maximal weight of W into his knapsack. 
# There are N items and the ith item weighs wi and is of value vi. Considering the 
# constraints of the maximum weight that a knapsack can carry, you have to find 
# and return the maximum value that a thief can generate by stealing items.

def solve(N,wi,vi,W):
    memo = {}
    def recurse_memo(idx, curr_w) -> int: # returns max value of items from index 0 to idx given the current capacity is curr_w 
        if (idx, curr_w) in memo: return memo[(idx, curr_w)]

        if idx == 0: 
            if wi[0] <= curr_w: return vi[0] # if the first element can be fit in the knapsack then add the value at the first index
            return 0 # else do not add anything to the value
        
        not_picked = 0 + recurse_memo(idx-1,curr_w)
        picked = float("-inf")
        if wi[idx] <= curr_w:
            picked = vi[idx] + recurse_memo(idx-1,curr_w-wi[idx])
        memo[(idx, curr_w)] = max(picked, not_picked)
        return memo[(idx, curr_w)]
    
    # return recurse_memo(N-1,W) # returns max_val of items from index 0 to N-1 given the current capacity is W

    def tabulation():
        dp = [[0]*(W+1) for _ in range(N)]
        # fill in the first row based on the capacity 'W'
        for idx in range(wi[0],W+1): dp[0][idx] = vi[0] # from wi[0] to W we returned vi[0]
        
        for idx in range(1,N):
            for curr_w in range(W+1):
                not_picked = 0 + dp[idx-1][curr_w]
                picked = float("-inf")
                if wi[idx] <= curr_w:
                    picked = vi[idx] + dp[idx-1][curr_w-wi[idx]]
                dp[idx][curr_w] = max(picked, not_picked)

        return dp[N-1][W]
    # return tabulation()

    def iteration():
        prev = [0]*(W+1)
        for idx in range(wi[0],W+1): prev[idx] = vi[0]

        for idx in range(1,N):
            temp = [0]*(W+1)
            # for curr_w in range(W+1):
            for curr_w in range(W,-1,-1): # this works too because we are not dependent on previous cols but only previous rows ergo we can optimize the space further by making changes to prev itself w/o initing a temp. this also works because after W-wi[idx] won't be on the right side of W in the array [0,W]. basically we are updating prev only for next iteration. going left to right does not work because we need prev values which get overriden if gone from left to right  
                not_picked = 0 + prev[curr_w]
                picked = float("-inf")
                if wi[idx] <= curr_w:
                    picked = vi[idx] + prev[curr_w-wi[idx]]
                temp[curr_w] = max(picked, not_picked)
            prev = temp
        return prev[W]
    # return iteration()

    def optimized_iter():
        prev = [0]*(W+1)
        for idx in range(wi[0],W+1): prev[idx] = vi[0]

        for idx in range(1,N):
            for curr_w in range(W,-1,-1): 
                not_picked = 0 + prev[curr_w]
                picked = float("-inf")
                if wi[idx] <= curr_w:
                    picked = vi[idx] + prev[curr_w-wi[idx]]
                prev[curr_w] = max(picked, not_picked)
        return prev[W]
    return optimized_iter()

N = 4
wi = [1,2,4,5] # weight 
vi = [5,4,8,6] # value
W = 5 # weight sum cannot exceed W and value should be maximum

print(solve(N,wi,vi,W)) # 13
