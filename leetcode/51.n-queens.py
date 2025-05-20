#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
from typing import List

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        all_solutions = []
        empty_board = [["." for _ in range(n)] for _ in range(n)]
        left_row_hashmap = [False]*n
        lower_left_diag_hashmap = [False]*(2*n-1)
        upper_left_diag_hashmap = [False]*(2*n-1)
    
        def generate_solution(col, board, left, lower, upper):
            if col >= n:
                all_solutions.append(["".join(row) for row in board])
                return
            
            for row in range(n):
                # if all the possible ways are not filled with "Q" ie are False, we can put a "Q"
                if not left[row] and not lower[row+col] and not upper[n-1+col-row]:
                    board[row][col] = "Q"
                    # now that it is filled mark it as filled and move on to the next column
                    left[row] = True
                    lower[row+col]  = True
                    upper[n-1+col-row] = True
    
                    generate_solution(col+1, board, left, lower, upper)
                    # when backtracking, remove the "Q" ie go back to making it empty and unmark the maps
                    board[row][col] = "."
                    left[row] = False
                    lower[row+col]  = False
                    upper[n-1+col-row] = False
    
        generate_solution(0, empty_board, left_row_hashmap, lower_left_diag_hashmap, upper_left_diag_hashmap)
        return all_solutions

# @lc code=end

