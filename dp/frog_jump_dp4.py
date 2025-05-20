# This is a follow-up question to “Frog Jump” discussed in the previous article. In the previous question, 
# the frog was allowed to jump either one or two steps at a time. In this question, the frog is allowed to 
# jump up to ‘K’ steps at a time. If K=4, the frog can jump 1,2,3, or 4 steps at every index.

def solve(n,k,arr):
    memo = {}
    def memoized_recursion(idx):
        if idx == 0: return 0
        if idx in memo: return memo[idx]

        # jump1 =  memoized_recursion(idx-1) + abs(arr[idx]-arr[idx-1])
        # if idx>1: jump2 = memoized_recursion(idx-2) + abs(arr[idx]-arr[idx-2])
        # if idx>2: jump3 = memoized_recursion(idx-3) + abs(arr[idx]-arr[idx-3])
        # return min(jump1, jump2, jump3)

        some_jump_cost = float("inf")
        for j in range(1,k+1):
            if idx >= j:
                jump_cost = memoized_recursion(idx-j) + abs(arr[idx]-arr[idx-j])
                some_jump_cost = min(some_jump_cost, jump_cost)

        memo[idx] = some_jump_cost
        return memo[idx]
    
    def tabulation():
        dp = [-1]*n
        dp[0] = 0
        for i in range(1,n):
            some_jump_cost = float("inf")
            for j in range(1,k+1):
                if i>=j:
                    jump_cost = memoized_recursion(i-j) + abs(arr[i]-arr[i-j])
                    some_jump_cost = min(some_jump_cost, jump_cost)
            dp[i] = some_jump_cost
        return dp[n-1]
    
    # return memoized_recursion(n-1) # top down 
    return tabulation()


arr = [30, 10, 60, 10, 60, 50]
k = 3
print(solve(len(arr), k, arr))

arr = [10,20,30,10]
k=2
print(solve(len(arr), k, arr))
