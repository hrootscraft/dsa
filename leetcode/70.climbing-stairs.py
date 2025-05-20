#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
    
        prev = 2
        second_to_prev = 1

        for _ in range(3, n + 1):
            current = prev + second_to_prev
            second_to_prev = prev
            prev = current

        return prev

        # if n == 1: return 1
        # elif n == 2: return 2
        # dp = [0] * (n + 1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]

        # def recurse(idx):
        #     if idx == 0: return 1 # standing at 0, there is only 1 way
        #     if idx == 1: return 1 # standing at 1, there is only 1 way
        #     return recurse(idx-1) + recurse(idx-2)
        # return recurse(n)

        # def recurse(curr_sum):
        #     if curr_sum > n: return 0
        #     if curr_sum == n: return 1
        #     return recurse(curr_sum + 1) + recurse(curr_sum + 2)
        # return recurse(0)
    
# @lc code=end

# Adobe, Alibaba, Amazon, Apple, Baidu, Bloomberg, Facebook, Goldman Sachs, Google,
# Huawei, LinkedIn, Microsoft, Oracle, TripAdvisor, Uber, Walmart Labs, Zulily 