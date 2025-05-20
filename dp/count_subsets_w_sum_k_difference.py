# This question is a slight modification of the problem discussed in Count Subsets with Sum K.
# We have the following two conditions given to us. (S1 and S2 are partitioned arrays' sums)
# S1 - S2 = D   – (i) 
# S1 >= S2     – (ii)

# now, we know S = S1+S2 - (iii), so from i and iii, (S-S2)-S2 = D ie S-2S2=D ie S2 = (S-D)//2
# ergo the problem becomes "find a subset with sum (S-D)//2". now, all array elements are whole 
# numbers so we know S-D cannot be negative but is greater than equal to zero so the edge case 
# is if S-D<0 return 0 and another edge case would be S2 can't be a fraction so when S-D is odd,
# we simply return a zero i.e item not included in the current_sum. and numbers in array are whole nos.

def solve(arr, D):
    n = len(arr)
    S = sum(arr)
    mod = 10**9 + 7 # since the answer can be large, it's asked to return modulo number of partitions 

    memo = {}
    def recurse_memo(idx, curr_sum): 
        if (idx,curr_sum) in memo: return memo[(idx,curr_sum)]

        if idx==0: 
            # if the target sum is 0 and the first index is also 0, 
            # like in case [0,1], we can form the subset in two ways, either 
            # by considering the first element or leaving it, so we can return 2
            if curr_sum == 0 and arr[0] == 0: return 2 

            # if target == 0, and the first element is not 0, we'll not pick the first element so just return 1 way.
            # when the first element is not 0, and the target is equal to the first element, we include it in the subset & return 1 way.
            elif curr_sum == 0 or curr_sum == arr[0]: return 1 
            return 0

        not_picked = recurse_memo(idx-1, curr_sum)
        picked = 0
        if arr[idx]<=curr_sum:
            picked = recurse_memo(idx-1, curr_sum-arr[idx])

        memo[(idx,curr_sum)] = (picked+not_picked)%mod
        return memo[(idx,curr_sum)]
    
    if (S-D)<0 or (S-D)%2==1: return 0 # no partitions can be made adhering to given conditions    
    target_sum = (S-D)//2
    # return recurse_memo(n-1,target_sum)

    def tabulation():
        dp = [[0]*(target_sum+1) for _ in range(n)]
        
        if arr[0] == 0: dp[0][0] = 2 # 2 cases - pick and not pick
        else: dp[0][0] = 1 # 1 case - not pick

        if arr[0] != 0 and arr[0] <= target_sum: dp[0][arr[0]] = 1 # 1 case - pick
        
        for idx in range(1,n):
            for curr_sum in range(target_sum+1):
                not_picked = dp[idx-1][curr_sum]
                picked = 0
                if arr[idx]<=curr_sum:
                    picked = dp[idx-1][curr_sum-arr[idx]]
                dp[idx][curr_sum] = (picked+not_picked)%mod
        
        return dp[n-1][target_sum]
    # return tabulation()

    def iteration():
        prev = [0]*(target_sum+1)
        if arr[0] == 0: prev[0] = 2
        else: prev[0] = 1
        if arr[0] != 0 and arr[0] <= target_sum: prev[arr[0]] = 1

        for idx in range(1,n):
            temp = [0]*(target_sum+1)
            for curr_sum in range(target_sum+1):
                not_picked = prev[curr_sum]
                picked = 0
                if arr[idx]<=curr_sum:
                    picked = prev[curr_sum-arr[idx]]
                temp[curr_sum] = (picked+not_picked)%mod
            prev = temp
        return prev[target_sum]
    return iteration()

arr = [5, 2, 5, 1]
D = 3

print(solve(arr,D)) # 2