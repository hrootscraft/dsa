#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
from typing import List
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # logically, if the subset is S then if we it partition into two subsets with the same sum then that sum=S/2
        # basically, we just find the subset with sum S/2. but when this sum is odd, then it is not possible to partition.
        target = sum(nums)
        if target%2 != 0: return False
        target = target//2
        n = len(nums)

        def iteration():
            prev = [False]*(target+1)
            for idx in range(n): prev[0] = True 
            if nums[0] <= target: prev[nums[0]] = True

            for idx in range(1, n):
                temp = [False]*(target+1)
                temp[0] = True
                for tgt in range(1, target+1):
                    not_picked = prev[tgt]
                    picked = False
                    if tgt >= nums[idx]: picked = prev[tgt-nums[idx]]
                    temp[tgt] = picked or not_picked
                prev = temp 
            return prev[target]
        return iteration()
    
# @lc code=end

#  Amazon, eBay, Facebook, Google, Microsoft, Paypal, Uber, VMware, Yahoo