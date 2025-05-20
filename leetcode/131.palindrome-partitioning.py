#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
from typing import List
# @lc code=start
class Solution:
    def is_partition_possible(self, start_idx: int, end_idx: int, s: str) -> bool:
        # check palindrome from start_idx to end_idx (inclusive)
        while start_idx < end_idx:
            if s[start_idx] != s[end_idx]:
                return False
            start_idx += 1
            end_idx -= 1
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def generate_solution(start_idx: int, current_solution: List[str]) -> None:
            if start_idx >= len(s):
                res.append(current_solution[:])
                return
            
            for end_idx in range(start_idx, len(s)):
                if self.is_partition_possible(start_idx, end_idx, s):
                    current_solution.append(s[start_idx: end_idx+1])
                    generate_solution(end_idx+1,current_solution)
                    current_solution.pop()
        
        generate_solution(0, [])
        return res
    
# @lc code=end

