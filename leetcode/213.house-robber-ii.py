#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
from typing import List
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        
        def iterative(arr):
            prev = arr[0]
            second_to_prev = 0
            for i in range(1,len(arr)):
                picked = arr[i]
                if i>1: picked += second_to_prev
                not_picked = 0 + prev
                curr_i = max(picked, not_picked) 
                second_to_prev = prev
                prev = curr_i
            return prev

        res_with_last_house = iterative(nums[1:])
        res_with_first_house = iterative(nums[:n-1])
        return max(res_with_last_house, res_with_first_house)
# @lc code=end

