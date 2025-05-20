#
# @lc app=leetcode id=2035 lang=python3
#
# [2035] Partition Array Into Two Arrays to Minimize Sum Difference
#

## refer /home/rutuja/dsa-python/dp/subsequence_target_bool.py tabulation method
from typing import List 
from functools import lru_cache

# @lc code=start
class Solution: 
    def minimumDifference(self, nums: List[int]) -> int:
        S = sum(nums) 
        n = len(nums)

        @lru_cache
        def recurse(idx, curr_sum, n_elements): # returns the min difference of 
            pass

       
# @lc code=end
