#
# @lc app=leetcode id=1547 lang=python3
#
# [1547] Minimum Cost to Cut a Stick
#
from typing import List
from functools import lru_cache
# @lc code=start
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        @lru_cache(maxsize=None)
        def recurse(idx, remaining_len_rod):
            pass
# @lc code=end

