#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

from typing import List
from collections import deque

# @lc code=start
class Solution:
    ## optimized previous submission by getting rid of the visited matrix, extra function, and a few more changes
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        # find starting rotten oranges and add them to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))

        minutes = 0

        while queue:
            # process all oranges in the current level
            level_size = len(queue)

            for _ in range(level_size):
                curr_r, curr_c = queue.popleft()

                # find valid neighbors and mark them as rotten
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # mark as rotten
                        queue.append((nr, nc))

            # increment minutes after processing all oranges in a level
            if queue:
                minutes += 1

        # check if there are any fresh oranges left
        for row in grid:
            if 1 in row: return -1 

        return minutes

# @lc code=end
    
#   Instead of performing BFS from each rotten orange independently, 
#   the algorithm performs a level-order traversal starting from all 
#   rotten oranges simultaneously. This way, the "minutes_passed" 
#   variable accurately reflects the minimum number of minutes required 
#   for all reachable fresh oranges to become rotten. Also, The line 
#   minutes_passed = max(minutes_passed, curr_min + 1) is necessary to 
#   ensure that minutes_passed always holds the maximum time it took for 
#   any orange to become rotten. This is crucial because the problem asks 
#   for the minimum number of minutes that must elapse until no cell has 
#   a fresh orange, which essentially is the time it took for the 
#   last fresh orange to become rotten :
    
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # n_rows, n_cols = len(grid), len(grid[0])
        # queue = deque()
        # n_fresh_oranges = 0

        # # initialize the queue with all rotten oranges and count fresh oranges
        # for row in range(n_rows):
        #     for col in range(n_cols):
        #         if grid[row][col] == 2:
        #             queue.append((row, col, 0))  # (row, col, minute)
        #         elif grid[row][col] == 1:
        #             n_fresh_oranges += 1

        # # perform BFS
        # minutes_passed = 0
        # while queue:
        #     curr_row, curr_col, curr_minute = queue.popleft()
        #     for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        #         new_row, new_col = curr_row + dr, curr_col + dc
        #         # if the neighbors are within bounds and are fresh
        #         if 0 <= new_row < n_rows and 0 <= new_col < n_cols and grid[new_row][new_col] == 1:
        #             grid[new_row][new_col] = 2  # make the orange rotten
        #             n_fresh_oranges -= 1  # decrease the count of fresh oranges
        #             queue.append((new_row, new_col, curr_minute + 1))
        #             minutes_passed = max(minutes_passed, curr_minute + 1)

        # # if there are any fresh oranges left, return -1
        # if n_fresh_oranges > 0: return -1
        # return minutes_passed

        n_rows, n_cols = len(grid), len(grid[0])
        queue = deque()
        n_fresh_oranges = 0

        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))  # adding rotten oranges with initial time 0
                elif grid[row][col] == 1:
                    n_fresh_oranges += 1  # counting fresh oranges

        if n_fresh_oranges == 0:  # edge case: no fresh oranges
            return 0

        while queue:
            curr_row, curr_col, curr_minute = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = curr_row + dr, curr_col + dc
                if 0 <= new_row < n_rows and 0 <= new_col < n_cols and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    n_fresh_oranges -= 1
                    queue.append((new_row, new_col, curr_minute + 1))

        return -1 if n_fresh_oranges > 0 else curr_minute  # use curr_minute directly
