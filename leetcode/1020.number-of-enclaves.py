from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # approach: go to the boundaries and start a dfs from all the unvisited 1s 
        # then by traversing all the univisited inner elements return the count of 1s
        n_rows, n_cols = len(grid), len(grid[0])

        def dfs(row, col):
            # if it's not a land or is out of bounds, return
            if not (0 <= row < n_rows and 0 <= col < n_cols) or grid[row][col] != 1:
                return
            # else mark the 1 as visited with 0 and go dfs on neighbors
            grid[row][col] = 0  
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = row + dr, col + dc
                dfs(nr, nc)

        for i in range(n_cols):
            dfs(0,i) # first row
            dfs(n_rows-1,i) # last row

        for i in range(n_rows):
            dfs(i,0) # first col
            dfs(i,n_cols-1) # last column

        # # above approach would be more efficient as its TC is 2*(n_rows+n_cols-2) while here it's n_rows*n_cols
        # for r in range(n_rows):
        #     for c in range(n_cols):
        #         if r==0 or c==0 or r=n_rows-1 or c==n_cols-1:
        #             if grid[r][c] == 1: dfs(r,c)

        # count remaining lands
        return sum(grid[r][c] == 1 for r in range(n_rows) for c in range(n_cols))
    
        # ## BFS-> SC: O(m*n) max space used by queue,  TC: O(m*n*4) 
        # # approach: go to the boundaries and start a bfs from all the unvisited 1s 
        # # then by traversing all the univisited inner elements return the count of 1s
        # n_rows, n_cols = len(grid), len(grid[0])
        # q = deque()

        # for i in range(n_cols):
        #     if grid[0][i] == 1: 
        #         grid[0][i] = 0
        #         q.append((0,i)) # first row
        #     if grid[n_rows-1][i] == 1: 
        #         grid[n_rows-1][i] = 0
        #         q.append((n_rows-1,i)) # last row

        # for i in range(n_rows):
        #     if grid[i][0] == 1: 
        #         grid[i][0] = 0
        #         q.append((i,0)) # first col
        #     if grid[i][n_cols-1] == 1: 
        #         grid[i][n_cols-1] = 0
        #         q.append((i,n_cols-1)) # last column

        # while q:
        #     curr_row, curr_col = q.popleft()
        #     for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        #         nr, nc = curr_row + dr, curr_col + dc
        #         if (0 <= nr < n_rows and 0 <= nc < n_cols) and grid[nr][nc] == 1:
        #             grid[nr][nc] = 0  
        #             q.append((nr, nc))

        # return sum(grid[r][c] == 1 for r in range(n_rows) for c in range(n_cols))

# sometimes recursion stack will take more time than bfs queue:
# BFS Accepted 18 minutes ago Python3 452 ms 18.1 MB
# DFS Accepted an hour ago Python3 454 ms 32.3 MB

