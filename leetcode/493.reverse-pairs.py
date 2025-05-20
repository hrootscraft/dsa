#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#
from typing import List
# @lc code=start
class Solution:
    def merge_and_count(self, low, mid, high, arr) -> int:
        count = 0
        merged = []
        arr1_start, arr2_start = low, mid + 1

        # count reverse pairs
        i, j = low, mid + 1
        while i <= mid: # for each of the element in the sorted left array check condition for that in sorted right array
            while j <= high and arr[i] > 2 * arr[j]:
                j += 1 # increment right pointer 
            count += j - (mid + 1)
            i += 1

        # merge two sorted arrays
        while arr1_start <= mid and arr2_start <= high:
            if arr[arr1_start] <= arr[arr2_start]:
                merged.append(arr[arr1_start])
                arr1_start += 1
            else:
                merged.append(arr[arr2_start])
                arr2_start += 1
        
        # directly append the remaining parts
        merged.extend(arr[arr1_start:mid+1])
        merged.extend(arr[arr2_start:high+1])

        # copy back to the original array
        arr[low:high+1] = merged
        return count

    def partition(self, low, high, arr) -> int:
        if low >= high: return 0 # no inversion for single element arrays or empty arrays
        mid = (low + high) // 2
        count = self.partition(low, mid, arr) # left count
        count += self.partition(mid + 1, high, arr) # add right count
        count += self.merge_and_count(low, mid, high, arr) # add merged count
        return count # left count + right count + merged count

    def reversePairs(self, nums: List[int]) -> int:
        return self.partition(0, len(nums)-1, nums)
    
# @lc code=end
# sol = Solution()
# nums = [2,4,3,5,1]
# print(sol.reversePairs(nums)) # 3