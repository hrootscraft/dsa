# given n, place n queens on a nxn chess board so that no queen can attack any of the other
# since a queen can attack in all the 8 directions, the implicit conditions here are:
# 1. each row must have 1 queen
# 2. each column must have 1 queen
# 3. no two queens should be able to attack each other

# Approach: we can use use backtracking here ie explore all possible solutions and 
# when one doesn't work out rollback to previous solution. this can be done with recursion

#__________________________________________________________________________
from typing import List

def is_possible_to_place_queen(row, col, board, n):
    # since we are iterating in the ascending direction of the column, 
    # we only need to check in 3 directions before placing the queen
    # and those are 1. left 2. top left (upper left diagonal) 3. bottom left (lower left diagonal)
    # so now, let's check top-left, left, and bottom-left directions for an existing queen

    row_copy, col_copy = row, col
    # 2 - check previous rows & columns for "Q"
    while row >= 0 and col >=0 :
        if board[row][col] == "Q": return False
        row -= 1
        col -= 1

    # 1 - check the same row but the previous columns for "Q"
    row, col = row_copy, col_copy
    while col >= 0:
        if board[row][col] == "Q": return False
        col -= 1

    # 3 - check the next rows and the previous columns for "Q"
    row, col = row_copy, col_copy
    while row < n and col >=0 :
        if board[row][col] == "Q": return False
        row += 1
        col -= 1

    return True

def n_queens(n: int) -> List[List[str]]: 
    all_solutions = []
    empty_board = [["." for _ in range(n)] for _ in range(n)] # [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]

    def generate_solution(col, board):
        if col >= n:
            # Convert each row to a string before adding to all_solutions
            all_solutions.append(["".join(row) for row in board])
            return
        
        for row in range(n):
            if is_possible_to_place_queen(row, col, board, n):
                board[row][col] = "Q"
                generate_solution(col+1, board)
                board[row][col] = "." # backtrack when the solution is not possible

    generate_solution(0, empty_board)
    return all_solutions
    
# print(n_queens(4))
# Here, for each of the three checks, we have O(n) TC so total O(3*n)
# and we do this n! times (for each row in generate_solution) so the TC is ~O(n!*n)
# SC here is O(n^2) 

#__________________________________________________________________________
# - we can make use of a hashmap to make the above is_possible_to_place_queen() more efficient
# - for the left direction we can store an array of n booleans
# - for the diagonals, the boolean array must be of size of 2*n-1. why? sum of indices in the 2D array can be stored in the grid tactfully
# - for lower left diagonal, we can check if row+col is marked/filled
# - for upper left diagonal, we can check if (n-1)+(col-row) is marked/filled

def n_queens_(n):
    all_solutions = []
    empty_board = [["."]*n for _ in range(n)]
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

print(n_queens_(4))
# in this optimized version , TC is the same O(n!*n) but SC is O(n)

# In the first solution, the space complexity is O(n^2) because of the board representation. 
# The board is represented as a 2D list with dimensions n x n, hence the space complexity 
# is proportional to the square of the board size, which is O(n^2).

# However, in the optimized solution, the space complexity is O(n). This is because instead 
# of storing the entire board, we only maintain arrays (left_row_hashmap, lower_left_diag_hashmap, 
# and upper_left_diag_hashmap) to keep track of which rows and diagonals are occupied by queens.