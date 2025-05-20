#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#
from typing import List

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # minimum ship capacity should be maximum of all weights because 
        # from given constraints, we need to ship all elements and if 
        # the ship capacity is lesser then either of the weights, 
        # then we cannot ship that weight but we are asked to ship ALL weights.
        # max ship capacity is sum of all weights, in this case we can ship all weights in a day
        # ergo our answer is in a range. therefore, we can use binary search

        # def is_possible_to_ship_all_in__d_days(cap):
        def find_days_to_ship_with_cap(cap):
            # returns the number of days needed to ship weights in a ship of capacity cap
            n_days = 1
            load = 0
            # on day 1 we initially have zero weight loaded
            # now while loading the ship, if capacity is exceeded, go to next day and load it else add to the load
            for w in weights:
                if load+w > cap:
                    n_days += 1
                    load = w
                else: load += w
            return n_days

        def linear_search():
            for cap in range(max(weights), sum(weights)+1):
                if find_days_to_ship_with_cap(cap) <= days: return cap
            return -1
        # return linear_search() # TC: O(n-squared) - TLE

        def bs(): # the minimum capacity will lie b/w max(weights) and sum(weights)
            low = max(weights)
            high = sum(weights)

            while low <= high:
                mid = (low+high)//2
                if find_days_to_ship_with_cap(mid) <= days:
                    high = mid-1 # eliminate right half and try a more minimum cap
                else:
                    low = mid+1 # eliminate left half try a higher a cap
            return low
        
        return bs() # TC: O(n* log2 n)

# @lc code=end

