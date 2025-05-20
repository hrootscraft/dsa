#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from typing import List
from collections import deque

class Solution:
    # # Approach 3: use a bfs traversal technique
    # # TC: O(2*n_rows*n_cols)
    # # SC: O(n_rows*n_cols)
    # # 1. Worst-case Scenario for Queue Size: In the absolute worst case, 
    # # where BFS might need to enqueue a significant portion of the grid before 
    # # dequeuing (e.g., a very zigzagging pattern that touches many cells), 
    # # the queue size could theoretically approach the size of the grid. 
    # # However, this scenario is highly constructed and not typical.
    # # 2. Typical Case: More realistically, the queue size at any given moment is 
    # # proportional to the "frontier" of the BFS exploration, which is related 
    # # to the breadth of the island being explored rather than the entire grid. 
    # # This means that while the queue size can grow, it is often constrained 
    # # by the actual shapes and distributions of islands within the grid.

    # # Thus, a more precise statement would be that the practical space complexity 
    # # in typical scenarios is related to the largest breadth of exploration at any time,
    # # which could be much less than MN in grids where land cells are not uniformly distributed.

    # # However, for strict worst-case analysis under theoretical conditions (like a maximally 
    # # dense and unfavorably configured grid that maximizes queue usage), one might still argue 
    # # for a space complexity of O(MN), recognizing this represents an upper bound rather 
    # # than the expected norm. The key takeaway is that, in practice, the BFS queue seldom, 
    # # if ever, needs to hold a significant fraction of the grid's cells simultaneously due to 
    # # the immediate marking of visited cells, which effectively limits the exploration frontier.

    # def numIslands(self, grid: List[List[str]]) -> int: 
    #     n_rows = len(grid)
    #     n_cols = len(grid[0])
    #     n_islands = 0
    #     # 0,1,2,3 -> top, right, bottom, left
    #     delta_row = [-1, 0, +1, 0]
    #     delta_col = [0, +1, 0, -1]

    #     def bfs(row,col):
    #         queue = deque([(row, col)])  # initialize the queue with the starting cell
    #         while queue:
    #             current_row, current_col = queue.popleft()  # dequeue the next cell to process
    #             for i in range(4):
    #                 new_row, new_col = current_row + delta_row[i], current_col + delta_col[i]
    #                 if 0 <= new_row < n_rows and 0 <= new_col < n_cols and grid[new_row][new_col] == '1':
    #                     grid[new_row][new_col] = '0'  # mark as visited
    #                     queue.append((new_row, new_col))  # enqueue this cell's unvisited neighbors

    #     for row in range(n_rows):
    #         for col in range(n_cols):
    #             # start bfs from each "unvisited land" cell
    #             if grid[row][col] == '1':
    #                 bfs(row,col)
    #                 n_islands += 1 # everytime you call dfs with a starting point, count increments
    #     return n_islands

    # Approach 2: recursive dfs with optimized space, instead of visited matrix we 
    # modify grid itself to indicate visited status (like changing 1s to 0s)
    # TC: O(2*n_rows*n_cols), SC: O(1)
    def numIslands(self, grid: List[List[str]]) -> int: 
        n_rows = len(grid)
        n_cols = len(grid[0])
        n_islands = 0
        # 0,1,2,3 -> top, right, bottom, left
        delta_row = [-1, 0, +1, 0]
        delta_col = [0, +1, 0, -1]

        def dfs(row,col):
            grid[row][col] = '0'
            
            for i in range(4):
                new_row, new_col = row + delta_row[i], col + delta_col[i]
                if 0 <= new_row < n_rows and 0 <= new_col < n_cols and grid[new_row][new_col] == '1':
                    dfs(new_row, new_col)

        for row in range(n_rows):
            for col in range(n_cols):
                # start dfs from each "unvisited land" cell
                if grid[row][col] == '1':
                    dfs(row,col)
                    n_islands += 1 # everytime you call dfs with a starting point, count increments
        return n_islands

    # # Approach 1: recursive dfs
    # # TC: traversal in the grid to check if it's an unvisited land, in the worst case all is land then n_rows*n_cols
    # #     dfs calls, for each piece of unvisited land, dfs is initiated, in the worst case it would visit each cell in the grid. hence, O(2*n_rows*n_cols)
    # # SC: visited array so n_rows*n_cols, recursion stack at the max it'll have to explore n_rows*n_cols. hence, O(2*n_rows*n_cols)
    # def numIslands(self, grid: List[List[str]]) -> int: 
    #     n_rows = len(grid)
    #     n_cols = len(grid[0])
    #     visited = [[False]*n_cols for _ in range(n_rows)]
    #     n_islands = 0
    #     # 0,1,2,3 -> top, right, bottom, left
    #     delta_row = [-1, 0, +1, 0]
    #     delta_col = [0, +1, 0, -1]

    #     def dfs(row,col):
    #         visited[row][col] = True
            
    #         for i in range(4):
    #             new_row, new_col = row + delta_row[i], col + delta_col[i]
    #             if 0 <= new_row < n_rows and 0 <= new_col < n_cols and not visited[new_row][new_col] and grid[new_row][new_col] == '1':
    #                 dfs(new_row, new_col)

    #     for row in range(n_rows):
    #         for col in range(n_cols):
    #             # start dfs from each "unvisited land" cell
    #             if grid[row][col] == '1' and not visited[row][col]:
    #                 dfs(row,col)
    #                 n_islands += 1 # everytime you call dfs with a starting point, count increments
    #     return n_islands
    
# @lc code=end
