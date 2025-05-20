# print longest increasing subsequence # refer leetcode 300
from functools import lru_cache
def solve(nums):
    n = len(nums)

    def tabulation():
        # curr_idx goes from 0 to n-1 while prev_idx goes from -1 to n-1
        # so to store -1 we shift it by 1 to the right ie -1~0, 0~1, 1~2, ...
        # so now prev_idx goes from 0 to n
        dp = [[1]*(n+1) for _ in range(n+1)]
        for prev_idx in range(n+1): dp[n][prev_idx] = 0

        for curr_idx in range(n-1,-1,-1):
            for prev_idx in range(n,-1,-1):
                not_picked = 0 + dp[curr_idx+1][prev_idx]
                picked = 0
                if prev_idx==0 or nums[curr_idx]>nums[prev_idx-1]: # adjust prev_idx
                    picked = 1 + dp[curr_idx+1][curr_idx+1] # adjust prev_idx
                dp[curr_idx][prev_idx] = max(picked,not_picked)
        
        # return dp[0][0]
        return dp
    
    dp = tabulation()
    print(dp)

solve([5,4,11,1,16,8])


