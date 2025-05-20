# We are given an array ‘ARR’ with N positive integers. We need to partition the array into 
# two subsets such that the absolute difference of the sum of elements of the subsets is minimum.
# We need to return only the minimum absolute difference of the sum of elements of the two partitions.
# eg. arr = [1,2,3,4] then min. abs. diff. is sum[1,4]-sum[2,3] = 0
# eg. arr = [8,6,5] then min. abs. diff. is sum[8]-sum[6,5] = 3

# refer /home/rutuja/dsa-python/dp/subsequence_target_bool.py tabulation method
# assuming S1 and S2 are sums of subsets of the array; now S1 can be max S(=sum(arr)) and so S2 will 0
# we need to minimize |S1-S2| but do we really need this? if we get all possible S1; min S1 is 0 
# when we don't pick any element in our subset and max is S. So, we use tabulation method and target as S+1

def solve(arr):
    n = len(arr)
    S = sum(arr)

    ## 1
    def tabulation():
        dp = [[False]*(S+1) for _ in range(n)]

        for idx in range(n): dp[idx][0] = True # if target==0: return True
        if arr[0]<=S: dp[0][arr[0]] = True  # if idx==0 and arr[0]==target: return True

        for idx in range(1,n):
            for target in range(1,S+1):
                not_picked = dp[idx-1][target]
                picked = False
                if arr[idx]<=target:
                    picked = dp[idx-1][target-arr[idx]]
                dp[idx][target] = picked or not_picked

        return dp
    
    # dp = tabulation() # last row of this has all possible S1
    # min_abs_diff = float("inf")
    # # for target in range(S+1): # target is S1
    # for target in range(S//2+1): # target is S1
    #     if dp[n-1][target]:
    #         S2 = S-target
    #         abs_diff = abs(target-S2)
    #         min_abs_diff = min(min_abs_diff, abs_diff)
    
    # return min_abs_diff


    ## 2
    def iteration():
        prev = [False]*(S+1)

        for idx in range(n): prev[0] = True # if target==0: return True
        if arr[0]<=S: prev[arr[0]] = True  # if idx==0 and arr[0]==target: return True

        for idx in range(1,n):
            temp = [False]*(S+1)
            for target in range(1,S+1):
                not_picked = prev[target]
                picked = False
                if arr[idx]<=target:
                    picked = prev[target-arr[idx]]
                temp[target] = picked or not_picked
            prev = temp

        return prev
    
    prev = iteration()
    min_abs_diff = float("inf")
    # for target in range(S+1): # target is S1
    for target in range(S//2+1): # target is S1
        if prev[target]:
            S2 = S-target
            abs_diff = abs(target-S2)
            min_abs_diff = min(min_abs_diff, abs_diff)
    
    return min_abs_diff

arr = [1,2,3,4]
print(solve(arr))

arr = [8,6,5]
print(solve(arr))

# We can optimize this because for targets in [0,S]
# we eventually get the same |S1-S2| after we cross the target=(S//2)+1
# so in the loop to find min we go from 0 to (S//2)+1


## space optimized
