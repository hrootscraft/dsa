#
# @lc app=leetcode id=2742 lang=python3
#
# [2742] Painting the Walls
#
from typing import List
from functools import cache
# @lc code=start
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n_walls = len(time)
        n = len(cost)

        @cache
        def recurse_memo(idx, walls_remaining) -> int: 
            if walls_remaining <= 0: return 0 # if there are no walls remaining, the function returns 0 because there's no cost associated with painting zero walls
            if idx < 0: return float("inf") # no feasile solution beyond this point

            not_picked = 0 + recurse_memo(idx-1,walls_remaining) # skip the current wall
            picked = cost[idx] + recurse_memo(idx-1,walls_remaining-time[idx]-1)
            return min(picked, not_picked)

        return recurse_memo(n-1, n_walls)
# @lc code=end

# Painter1 takes cost[i] amount and time[i] time to paint i th wall. 
# When the Painter1 is busy painting a wall, Painter2 can paint other walls in 0 cost and unit time. 
# So, we understand that whether Painter2 will be able to paint a wall depends on Painter1. 
# Thus, let's eliminate Painter2 for the time being & focus on Painter 1. 
# So, the problem boils down to the conclusion of picked and not_picked case of Painter1; 
# When Painter1 will be busy, we will simply not_pick any wall. Why? Because when Painter1 will be busy 
# we will change the number of wall remaining to : walls - time[i] - 1(-1 for current wall and time[i] 
# are the walls painted by free painter or Painter2). Thus, this compensates for the Painter2. 
# Therefore, the problem boils down to the classical 0/1 knapsack where weight array is time and value array is cost
# We minimize the cost (or maximize value in knapsack)