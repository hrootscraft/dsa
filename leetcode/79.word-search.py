#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
from typing import List
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_rows, n_cols = len(board), len(board[0])
        
        def dfs(r,c,idx) -> bool:
            if idx == len(word): return True

            # if the cell is out of bounds or if word[idx] is not present at the cell or the cell is visited
            if not (0 <= r < n_rows and 0 <= c < n_cols) or board[r][c] != word[idx] or board[r][c] == "#":
                return False
            
            # mark cell as visited (avoid unnecessary backtracking)
            board[r][c] = "#"

            for dr,dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r+dr, c+dc
                if dfs(nr, nc, idx+1): return True

            # backtrack (reset visited cell)
            board[r][c] = word[idx]
            return False

        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0): return True
        return False

# @lc code=end

# asked in Aetion, Amazon, Apple, Bloomberg, ByteDance, Cruise, Automation, 
# Docusign, Facebook, Google, Intuit, caMorgan, LinkedIn, Lyft, Microsoft, 
# Oracle, Pinterest, Quantcast, Snapchat, Uber, Yahoo, Zillow
    
# TC : O(N * 3^L) where N = n_rows*n_cols and L=len(word); N because we may need 
# to start a dfs from all cells and 3^L because technically we may need to explore 
# all 3 directions for L times as we already check for the cell where we came from "#"
    
# SC: O(N) recursion stack in worst case may hold all cells