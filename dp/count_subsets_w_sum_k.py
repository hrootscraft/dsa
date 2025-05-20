def solve(arr, k):
    n = len(arr)
    memo = {}

    def recurse_memo(idx, curr_sum): 
        if (idx,curr_sum) in memo: return memo[(idx,curr_sum)]
        if curr_sum==0: return 1 # assuming all numbers in array are positive 
        if idx==0: return arr[idx]==curr_sum # return 1(or true) if the first array element is making up for the curr_sum remaining ie take it into the subset

        not_picked = recurse_memo(idx-1, curr_sum)
        picked = 0
        if arr[idx]<=curr_sum:
            picked = recurse_memo(idx-1, curr_sum-arr[idx])

        memo[(idx,curr_sum)] = picked+not_picked
        return memo[(idx,curr_sum)]
    # return recurse_memo(n-1,k)

    def tabulation():
        dp = [[0]*(k+1) for _ in range(n)]
        for idx in range(n): dp[idx][0] = 1
        if arr[0] <= k: dp[0][arr[0]] = 1

        for idx in range(1,n):
            for curr_sum in range(1,k+1):
                not_picked = dp[idx-1][curr_sum]
                picked = 0
                if arr[idx]<=curr_sum:
                    picked = dp[idx-1][curr_sum-arr[idx]]
                dp[idx][curr_sum] = picked+not_picked
        
        return dp[n-1][k]
    # return tabulation()

    def iteration():
        prev = [0]*(k+1)
        prev[0] = 1
        if arr[0] <= k: prev[arr[0]] = 1

        for idx in range(1,n):
            temp = [0]*(k+1)
            temp[0] = 1
            for curr_sum in range(1,k+1):
                not_picked = prev[curr_sum]
                picked = 0
                if arr[idx]<=curr_sum:
                    picked = prev[curr_sum-arr[idx]]
                temp[curr_sum] = picked+not_picked
            prev = temp
        return prev[k]
    return iteration()

arr = [1, 2, 2, 3]
k = 3 # the sum of subset

print(solve(arr,k))