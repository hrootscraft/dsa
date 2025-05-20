from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Asked in  Amazon, Facebook, Google, Splunk, Uber  

        Approach: start a dfs from the O's on the boundary of the board and mark them as "cannot be captured" and mark the rest as X's  
        """
        n_rows, n_cols = len(board), len(board[0])
        # visited = [[False]*n_cols for _ in range(n_rows)]
        
        # def dfs(row,col):
        #     if not (0<=row<n_rows and 0<=col<n_cols) or visited[row][col] or board[row][col] != "O":
        #         return
        #     visited[row][col] = True
        #     for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        #         nr, nc = row+dr, col+dc
        #         dfs(nr, nc)

        def dfs(row, col):
            if not (0 <= row < n_rows and 0 <= col < n_cols) or board[row][col] != "O":
                return
            board[row][col] = "V"  # Mark the 'O' as visited
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = row + dr, col + dc
                dfs(nr, nc)

        for i in range(n_cols):
            if board[0][i] == "O" and board[0][i] != "V": dfs(0,i) # first row
            if board[n_rows-1][i] == "O" and board[n_rows-1][i] != "V": dfs(n_rows-1,i) # last row

        for i in range(n_rows):
            if board[i][0] == "O" and board[i][0] != "V": dfs(i,0) # first col
            if board[i][n_cols-1] == "O" and board[i][n_cols-1] != "V": dfs(i,n_cols-1) # last column

        # for r in range(n_rows):
        #     for c in range(n_cols):
        #         if not visited[r][c]:
        #             board[r][c] = "X"

        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "V":
                    board[r][c] = "O"

        return board