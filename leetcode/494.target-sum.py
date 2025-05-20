#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from typing import List
# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total_sum = sum(nums)   

        # memo = {}
        # def recurse_memo(idx, target):
        #     if (idx,target) in memo: return memo[(idx,target)]
        #     if idx == 0:  
        #         # if target+nums[idx] == 0: return 1
        #         # if target-nums[idx] == 0: return 1
        #         # return 0

        #         # handle zeroes in the array seperately
        #         if nums[idx] == 0: # if the first element is zero then adding and subtracting will both give correct answer if further target is already zero so we return 2 as the count
        #             if target == 0: return 2
        #             else: return 0
        #         elif target == nums[idx] or target == -nums[idx]: return 1
        #         else: return 0

        #     left = recurse_memo(idx-1, target+nums[idx])
        #     right = recurse_memo(idx-1, target-nums[idx])
        #     memo[(idx,target)] = left+right
        #     return memo[(idx,target)]

        # # return recurse_memo(n-1,target)

        # def incorrect_tabulation():
        #     dp = [[0]*(target+1) for _ in range(n)]

        #     for tgt in range(target+1): # no need to do this because we will encounter negative targets which is not taken into account here
        #         if nums[0] == 0: 
        #             if tgt == 0: dp[0][0] = 2
        #             else: dp[0][0] = 0
        #         if tgt == nums[0] or tgt == -nums[0]: dp[0][tgt] = 1 # but here, we might get negative indices and so it needs to be handled. 
        #         else: dp[0][tgt] = 0

        #     for idx in range(1,n):
        #         for tgt in range(target+1):
        #             left = dp[idx-1][tgt+nums[idx]]
        #             right = dp[idx-1][tgt-nums[idx]]
        #             dp[idx][tgt] = left+right

        #     return dp[n-1][target]
        # # return incorrect_tabulation()

        # def corrected_tabulation():
        #     if abs(target) > total_sum: return 0 # there's no way we can create target with given array elements

        #     # dp[idx][tgt] represents the number of ways to reach the target (tgt-total_sum) using the first idx+1 elements of nums
        #     dp = [[0]*(2*total_sum+1) for _ in range(n)] # takes into account all possible targets [-total_sum, total_sum]
        #     ## the above is as good as adding a huge number to the target and finding it like so:
        #     ## dp = [[0]*(2001) for _ in range(n)] # because -1000<=target<=1000

        #     # handling the base case (when idx == 0)
        #     # for the first element, we handle zeros separately
        #     if nums[0] == 0:
        #         dp[0][total_sum] = 2 # since we're adding total_sum to the target to account for negative numbers, condition for when tgt==0 will be equivalent to tgt==total_sum
        #     else:
        #         dp[0][total_sum+nums[0]] = 1
        #         dp[0][total_sum-nums[0]] = 1

        #     for idx in range(1, n):
        #         for tgt in range(2*total_sum+1):
        #             if tgt+nums[idx] <= 2 * total_sum:
        #                 left = dp[idx-1][tgt+nums[idx]]
        #             else: left = 0
        #             if tgt-nums[idx] >= 0:
        #                 right = dp[idx-1][tgt-nums[idx]]
        #             else: right = 0
        #             dp[idx][tgt] = left+right

        #     return dp[n-1][target+total_sum]
        # # return corrected_tabulation()

        # def iteration():
        #     if abs(target) > total_sum: return 0

        #     prev = [0]*(2*total_sum+1) 

        #     if nums[0] == 0:
        #         prev[total_sum] = 2 
        #     else:
        #         prev[total_sum+nums[0]] = 1
        #         prev[total_sum-nums[0]] = 1

        #     for idx in range(1, n):
        #         temp = [0]*(2*total_sum+1) 
        #         for tgt in range(2*total_sum+1):
        #             if tgt+nums[idx] <= 2 * total_sum:
        #                 left = prev[tgt+nums[idx]]
        #             else: left = 0
        #             if tgt-nums[idx] >= 0:
        #                 right = prev[tgt-nums[idx]]
        #             else: right = 0
        #             temp[tgt] = left+right

        #         prev = temp

        #     return prev[target+total_sum]
        # return iteration()

        ## There is another approach we can use: find the ways in which we can divide nums into 2 parts so that the difference of sum of those parts equals the given target
        ## Basically, what we're doing here is give one part a plus sign and the other a negative sign and add them up to get their difference which should equal to target
        ## Refer /home/rutuja/dsa-python/dp/count_subsets_w_sum_k_difference.py for further explanation
        # S1+S2 = total_sum where S1 & S2 are sums of partioned arrays
        # S1-S2 = target where S1>=S2 
        # therefore, S2 = (total_sum-target)//2 and so the problem boils down to find a subset of nums array with this sum S2
        target_sum = (total_sum-target)//2 # we have to find a subset from nums with sum=target_sum
        memo = {}
        def approach2_recurse_memo(idx, target):
            if (idx,target) in memo: return memo[(idx,target)]

            if idx==0:
                if target==0 and nums[0]==0: return 2
                elif target == 0 or target == nums[0]: return 1 
                return 0
            
            not_picked = approach2_recurse_memo(idx-1, target)
            picked = 0
            if nums[idx]<=target:
                picked = approach2_recurse_memo(idx-1, target-nums[idx])

            memo[(idx,target)] = picked+not_picked
            return memo[(idx,target)]

        if (total_sum-target)<0 or (total_sum-target)%2==1: return 0 # S2 can't be negative or a fraction
        # return approach2_recurse_memo(n-1,target_sum)

        def approach2_tabulation():
            dp = [[0]*(target_sum+1) for _ in range(n)]

            if nums[0] == 0: dp[0][0] = 2 # 2 cases - pick and not pick
            else: dp[0][0] = 1 # 1 case - not pick

            if nums[0] != 0 and nums[0] <= target_sum: dp[0][nums[0]] = 1 # 1 case - pick

            for idx in range(1,n):
                for curr_sum in range(target_sum+1):
                    not_picked = dp[idx-1][curr_sum]
                    picked = 0
                    if nums[idx]<=curr_sum:
                        picked = dp[idx-1][curr_sum-nums[idx]]
                    dp[idx][curr_sum] = picked+not_picked

            return dp[n-1][target_sum]
        # return approach2_tabulation()
    
        def approach2_iteration():
            prev = [0]*(target_sum+1)
            if nums[0] == 0: prev[0] = 2
            else: prev[0] = 1
            if nums[0] != 0 and nums[0] <= target_sum: prev[nums[0]] = 1

            for idx in range(1,n):
                temp = [0]*(target_sum+1)
                for curr_sum in range(target_sum+1):
                    not_picked = prev[curr_sum]
                    picked = 0
                    if nums[idx]<=curr_sum:
                        picked = prev[curr_sum-nums[idx]]
                    temp[curr_sum] = picked+not_picked
                prev = temp
            return prev[target_sum]
        return approach2_iteration()

# @lc code=end

#  Facebook, Google, Microsoft 

            