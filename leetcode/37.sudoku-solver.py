#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
from typing import List
# @lc code=start
class Solution:
    # here, we are required to return only one solution for the soduko problem 
    def is_possible(self, board: List[List[str]], row: int, col: int, c: int) -> bool:
        # now we can check for row, column, and small grid condition in
        # one iteration itself instead of doing 3 different traversals
        for i in range(len(board)):
            # if the number is already in that row, return False
            if board[i][col] == c: return False
            # if the number is already in that column, return False
            if board[row][i] == c: return False
            # if the number is already in that grid, return False
            if board[3*(row//3) + i//3][3*(col//3) + i%3] == c: return False
        return True

    def solve(self, board: List[List[str]]) -> bool:
        # explore empty cell 
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".": # empty cell encountered
                    for c in "123456789": # now try to fill it with feasible number
                        if self.is_possible(board, row, col, c):
                            board[row][col] = c
                            if self.solve(board): return True
                            board[row][col] = "."
                    # when out of the for loop it means no number was placed or no possible solution found so,
                    return False
        # last condition is we never find an empty cell in the board, in that case the soduko is already solved so,
        return True    

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)
                    
# @lc code=end
        
    # 3*(row//3) and 3*(col//3) move us to the top-left cell of the target sub-grid.
    # i//3 moves us down 0, 1, or 2 rows within the sub-grid, based on the value of i.
    # i%3 moves us right 0, 1, or 2 columns within the sub-grid, based on the value of i.

