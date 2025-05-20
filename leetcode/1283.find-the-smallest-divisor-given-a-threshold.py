#
# @lc app=leetcode id=1283 lang=python3
#
# [1283] Find the Smallest Divisor Given a Threshold
#
from typing import List
import math

# @lc code=start
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # the solution lies between 1 and size of the array because 
        # for a very high value of divisor, the sum will size of array
        # so we can take the max element from the array and use it as 
        # higehr limit of the range
        def is_possible_solution(divisor, nums):
            conditional_arr_sum = sum(math.ceil(num/divisor) for num in nums)
            return conditional_arr_sum <= threshold

        def bs(nums, threshold):
            if len(nums) > threshold: return -1

            low = 1
            high = max(nums)

            while low<=high:
                mid = (low+high)//2
                if is_possible_solution(mid, nums):high = mid-1
                else: low = mid+1
            return low
        
        return bs(nums, threshold)
                
# @lc code=end

