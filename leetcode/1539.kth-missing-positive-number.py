#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#
from typing import List
# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # def linear_search(k): # TC: O(n) and SC: O(1)
        #     for num in arr:
        #         if num <= k: k += 1
        #         else: break # Stops the loop but continues to return k after processing all iterations (or on break). Continues checking subsequent elements after num <= k. Returns the final k after the loop.
        #     return k 

        # def linear_search(k): # wrong answer
        #     for num in arr:
        #         if num <= k: k += 1
        #         else: return k # Exits the loop and the function immediately upon num > k. Stops checking further elements as soon as num > k is found. Returns k at the point where num > k.

        # return linear_search(k)

        # to optimize the solution, we can try Binary Search but we cannot apply the BS on answer space because we aren't finding max or min in a range here.
        # we'll do something different here. we try to find the closest neighbors (present in the array) for the kth missing number by counting the number of missing numbers for each element in the given array.
        # for arr=[2, 3, 4, 7, 11], 
        # uptil index 0: Only 1 number ((2-1) -> (num in array - num that should have been there)) i.e. 1 is missing in the given array
        # uptil index 1: Only 1 number (3-2) i.e. 1 is missing in the given array
        # uptil index 2: Only 1 number (4-3) i.e. 1 is missing in the given array
        # uptil index 3: 3 numbers (7-4) i.e. 1, 5, and 6 are missing
        # uptil index 4: 6 numbers (11-5) i.e. 1, 5, 6, 8, 9, and 10 are missing
        # for k=5, we can determine that the answer falls within the range of 7 to 11. 
        # since there are only 3 missing numbers uptil index 3, the 5th missing number 
        # cannot be before arr[3], which is 7. therefore, it must be located somewhere to the right 
        # of 7. our actual answer 9 also supports this theory. 
        # simply, if arr=[2, 3, 4, 7, 11], then n_missing_at_corresponding_idx_arr=[1, 1, 1, 3, 6]
        def bs(arr, k):
            low = 0
            high = len(arr)-1

            while low <= high:
                mid = (low+high)//2
                n_missing_at_idx = arr[mid] - (mid+1)
                if n_missing_at_idx < k:
                    low = mid+1 # eliminate left half
                else: high = mid-1 # eliminate right half

            # at this point we have our high and low pointing to left and right closest neighbors between which kth missing value is
            # return arr[high]+(more_to_complete_k_missing) # this cannot be done because for arr=[4,7,11] and k=3, high=-1
            # but, if we formulate this number to be returned, we don't actually need to access arr[high]
            # n_missing_at_high = arr[high]-(high+1) = arr[high]-high-1 
            # more_to_complete_k_missing = k-n_missing_at_high = k-(arr[high]-high-1) = k-arr[high]+high+1 
            # kth_missing = arr[high]+more_to_complete_k_missing = arr[high]+k-arr[high]+high+1 = k+high+1

            # return k+high+1 # orrr do the following
            return k+low
        
        return bs(arr, k)
# @lc code=end

