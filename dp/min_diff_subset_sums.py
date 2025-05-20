# We are given an array ‘ARR’ with N positive integers. We need to partition the array into two subsets 
# such that the absolute difference of the sum of elements of the subsets is minimum.

# prereq: subsequence_target_bool.py

def min_diff_of_sums_of_subsets(nums):
    # let S1 be sum of 1st subset and S2 the sum of 2nd
        S = sum(nums) # S is the target
        n = len(nums)

        # # TC: O(n*S//2), SC: O(n*(S//2))
        # dp = [[False]*(S//2+1) for _ in range(n)] # rows-index-from 0 to n-1, cols-target sum-from 0 to S+1
        # for idx in range(n): dp[idx][0] = True
        # if nums[0] <= S: dp[0][nums[0]] = True
        # for idx in range(1,n):
        #     for target in range(1,S//2+1):
        #         not_picked = dp[idx-1][target]
        #         picked = False
        #         if nums[idx] <= target: picked = dp[idx-1][target-nums[idx]]
        #         dp[idx][target] = picked or not_picked

        # min_diff = float("inf") 
        # for S1 in range(S//2+1):
        #     if dp[n-1][S1]:     
        #         min_diff = min(min_diff, abs((S-S1)-S1))
        # return min_diff

        # TC: O(n*S//2), SC: O(S//2)
        prev = [False]*(S//2+1)
        for idx in range(n): prev[0] = True
        if nums[0] <= S: prev[nums[0]] = True
        for idx in range(1,n):
            temp = [False]*(S//2+1)
            for target in range(1,S//2+1):
                not_picked = prev[target]
                picked = False
                if nums[idx] <= target: picked = prev[target-nums[idx]]
                temp[target] = picked or not_picked
            prev = temp

        min_diff = float("inf") 
        for S1 in range(S//2+1):
            if prev[S1]:     
                min_diff = min(min_diff, abs((S-S1)-S1))
        return min_diff

print(min_diff_of_sums_of_subsets([3, 1, 5, 2, 8])) # 1