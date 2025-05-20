#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#
from typing import List

# @lc code=start
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        def is_bouquet_possible_2(days_to_wait, m, k, bloomDay):
            counter = 0
            n_bouquets = 0
            
            for day in bloomDay:
                if day <= days_to_wait:
                    counter += 1
                    if counter == k: # if we have enough adjacent flower, make a bouquet and set the counter to zero to start counter next set of adjacent flowers
                        n_bouquets += 1
                        counter = 0
                        if n_bouquets >= m: # early return if we can make enough required bouquets
                            return True
                else:
                    counter = 0 # reset counter when flower is not bloomed
            
            return n_bouquets >= m

        def is_bouquet_possible(days_to_wait, m, k, bloomDay):
            counter = 0 # counter to keep track adjacent flowers
            n_bouquets = 0

            for day in bloomDay:
                if day <= days_to_wait: # if bloomed
                    counter += 1
                else:
                    n_bouquets += counter//k # for the so far `counter` adjacent flowers counter//k bouquets are possible
                    counter = 0 # reset the counter for non-bloomed flower

            n_bouquets += counter//k
            return n_bouquets >= m

        def bs(bloomDay, m, k): # required min day falls between min and max of bloomDay
            low = min(bloomDay)
            high = max(bloomDay)

            while low<=high:
                mid = (low+high)//2
                if is_bouquet_possible(mid, m, k, bloomDay): # performs better
                # if is_bouquet_possible_2(mid, m, k, bloomDay):
                    high = mid-1
                else:
                    low = mid+1
            return low
        
        return bs(bloomDay, m, k)

# @lc code=end

