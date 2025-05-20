#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
from typing import List

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []

        def generate_subset(idx, current_subset):
            all_subsets.append(current_subset[:])
            for i in range(idx, len(nums)):
                current_subset.append(nums[i])
                generate_subset(i+1, current_subset)
                current_subset.pop()
        
        generate_subset(0, [])
        return all_subsets


        # all_subsets = []

        # def generate_subset(idx, current_subset):
        #     all_subsets.append(current_subset[:])
        #     for i in range(idx, len(nums)):
        #         generate_subset(i+1, current_subset + [nums[i]])
        
        # generate_subset(0, [])
        # return all_subsets
    
    
        # n = len(nums)
        # all_subsets = []
        # total_subsets = 1 << n  # returns 2^n

        # for num in range(total_subsets):
        #     subset = []
        #     # check each bit of the current number 'num'
        #     for i in range(n):
        #         # if "i"th bit of num is set, include the corresponding element from 'nums'
        #         if (num & (1 << i)) > 0:
        #             subset.append(nums[i])
        #     all_subsets.append(subset)

        # return all_subsets
    

        # n = len(nums)
        # all_subsets = []

        # def generate_subset(idx, current_subset):
        #     if idx >= n: 
        #         all_subsets.append(current_subset[:])
        #         return
            
        #     generate_subset(idx+1, current_subset+[nums[idx]])
        #     generate_subset(idx+1, current_subset)

        # generate_subset(0, [])
        # return all_subsets

# @lc code=end

