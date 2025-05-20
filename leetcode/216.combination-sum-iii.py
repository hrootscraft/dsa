#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        all_subsets = []

        def generate_subset(idx, current_subset, current_sum):
            if len(current_subset)==k and current_sum == n:
                all_subsets.append(current_subset[:])
                return
            
            if len(current_subset) > k or current_sum > n or idx > 9: return
            
            for i in range(idx, 10):
                generate_subset(i+1, current_subset+[i], current_sum+i)

        generate_subset(1,[],0)
        return all_subsets
        
# @lc code=end

