# Problem Statement:

# Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. 
# At a time the frog can climb either one or two steps. A height[N] array is also given. 
# Whenever the frog jumps from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), 
# where abs() means the absolute difference. We need to return the minimum energy 
# that can be used by the frog to jump from stair 0 to stair N-1.

# Eg. height = [10,20,30,10], N=4
# solution=20 because jumps: idx 0->1 (|20-10|=10) and 1->3 (|10-20|=10)

def solve(n, arr) -> int:

    def recurse(idx) -> int:
         # the energy to reach from 0 to 0 index is 0
        if idx == 0: return 0
        # handling base case for invalid indices, since we compare and want the 
        # minimum energy we assign the invalid ones infinity so it does not get picked
        if idx < 0: return float('inf') 

        left = recurse(idx-1) + abs(arr[idx]-arr[idx-1])
        right = float('inf') # initialize right with infinity
        
        if idx > 1: # if standing at 1, one cannot jump 2 steps, idx will then be -1
            right = recurse(idx-2) + abs(arr[idx]-arr[idx-2])
            
        return min(left, right)
    
    def memoization(idx, memo) -> int:
        if idx == 0: return 0
        if idx < 0: return float("inf")
        if idx in memo: return memo[idx]

        left = memoization(idx-1, memo) + abs(arr[idx]-arr[idx-1])
        right = float('inf')

        if idx > 1: right = memoization(idx-2, memo) + abs(arr[idx]-arr[idx-2])
        memo[idx] = min(left, right)
        return memo[idx]
    
    def tabulation() -> int:
        dp = [-1]*(n) # stores the energy required to to jump from i to 0 where i->[0,n-1]
        dp[0] = 0
        for i in range(1,n):
            left = dp[i-1] + abs(arr[i]-arr[i-1])
            right = float('inf')
            if i>1: right = dp[i-2] + abs(arr[i]-arr[i-2])
            dp[i] = min(left,right)
        return dp[n-1]
    
    def iteration() -> int:
        prev, second_to_prev = 0, 0
        for i in range(1,n):
            left = prev + abs(arr[i]-arr[i-1])
            right = float('inf')
            if i>1: right = second_to_prev + abs(arr[i]-arr[i-2])
            curr_i = min(left,right)
            second_to_prev = prev
            prev = curr_i
        return prev

    # return recurse(n-1) # return the minimum energy needed to reach n-1 index
    # return memoization(n-1, {})
    # return tabulation() # bottom up approach
    return iteration()

print(solve(4, [10,20,30,10])) # 20