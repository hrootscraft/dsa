## subsequence can have non-consecutive elements but the order has to be same
## in substring the elements are consecutive as well as the order is the same

def solve(s1,s2):
    n = len(s1)
    m = len(s2)
    res = 0

    ## tabulation code:
    # dp = [[0]*(m+1) for _ in range(n+1)]
    # for idx1 in range(n):
    #     for idx2 in range(m):
    #         if s1[idx1] == s2[idx2]:
    #             dp[idx1][idx2] = dp[idx1-1][idx2-1] + 1
    #             res = max(res, dp[idx1][idx2])
    #         else: dp[idx1][idx2] = 0

    ## space optimized:
    prev = [0]*(m+1)
    for idx1 in range(n):
        curr = [0]*(m+1)
        for idx2 in range(m):
            if s1[idx1] == s2[idx2]:
                curr[idx2] = prev[idx2-1] + 1
                res = max(res, curr[idx2])
            else: curr[idx2] = 0
        prev = curr
        
    return res

s1 = "abcjklp"
s2 = "acjkp"
## here, longest common subsequence is acjkp but longest common substring is cjk
print(solve(s1,s2))