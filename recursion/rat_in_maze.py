# Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). 
# Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat 
# can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is 
# blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
# Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

# Example 1:
# Input:
# N = 4
# m[][] = {{1, 0, 0, 0},
#          {1, 1, 0, 1}, 
#          {1, 1, 0, 0},
#          {0, 1, 1, 1}}
# Output:
# DDRDRR DRDDRR
# Explanation:
# The rat can reach the destination at 
# (3, 3) from (0, 0) by two paths - DRDDRR 
# and DDRDRR, when printed in sorted order 
# we get DDRDRR DRDDRR.

# Example 2:
# Input:
# N = 2
# m[][] = {{1, 0},
#          {1, 0}}
# Output:
# -1
# Explanation:
# No path exists and destination cell is 
# blocked.

# Your Task:  
# Complete the function printPath() which takes N and 2D array m[ ][ ] as input parameters and returns the list of paths in lexicographically increasing order. 
# Note: In case of no path, return an empty list. The driver will output "-1" automatically.

# Expected Time Complexity: O((3N^2)).
# Expected Auxiliary Space: O(L * X), L = length of the path, X = number of paths.

# Constraints:
# 2 ≤ N ≤ 5
# 0 ≤ m[i][j] ≤ 1

from typing import List

def findPath(maze: List[List[int]], n: int) -> List[str]:
    all_solutions = []
    visited = [[False]*n for _ in range(n)]
    
    def generate_path(row, col, current_path, visited) -> None:
        # base condition: if the 
        if row == n-1 and col == n-1:
            all_solutions.append(current_path)
            return
        
        ## since, we are required to return the list of paths in lexicographical order, 
        ## we'll call the recursive functions in that same order - DLRU

        # downward
        if row+1 < n and not visited[row+1][col] and maze[row+1][col] == 1:
            visited[row][col] = True
            generate_path(row+1, col, current_path+'D', visited)
            visited[row][col] = False

        # left
        if col-1 >= 0 and not visited[row][col-1] and maze[row][col-1] == 1:
            visited[row][col] = True
            generate_path(row, col-1, current_path+'L', visited)
            visited[row][col] = False

        # right
        if col+1 < n and not visited[row][col+1] and maze[row][col+1] == 1:
            visited[row][col] = True
            generate_path(row, col+1, current_path+'R', visited)
            visited[row][col] = False

        # upward
        if row-1 >= 0 and not visited[row-1][col] and maze[row-1][col] == 1:
            visited[row][col] = True
            generate_path(row-1, col, current_path+'U', visited)
            visited[row][col] = False

    if maze[0][0] == 1:
        generate_path(0,0,"", visited)

    if not len(all_solutions): return -1
    return all_solutions

maze = [[1, 0, 0, 0],
        [1, 1, 0, 1], 
        [1, 1, 0, 0],
        [0, 1, 1, 1]]
n = 4

maze_1 = [[1, 0],
          [1, 0]]
n_1 = 2
# print(findPath(maze, n))
# print(findPath(maze_1, n_1))

## Here, the TC is O(4^(n*n))
# At each cell, there are up to 4 directions to explore (up, down, left, right), 
# and for each cell, we make recursive calls to explore these directions.
# Therefore, the total number of recursive calls can be as high as 4^(m*n).

## And, the SC is O(n*n) 
# The maximum depth of the recursion tree (the number of recursive calls on the call stack) 
# can be at most m*n, which corresponds to visiting every cell in the maze.
# Additionally, the auxiliary space used by the visited matrix is also O(m*n), 
# as it stores information about whether each cell has been visited.
# The all_solutions list will store all valid paths, which can be up to O(2^n) 
# in the worst case, where n is the number of cells in the maze.

# def input_maze(N):
#     maze = []
#     print("Enter the maze matrix (0 for blocked cell, 1 for open cell):")
#     for _ in range(N):
#         row = list(map(int, input().split()))
#         maze.append(row)
#     return maze

# N = int(input("Enter the square maze dimension N: "))
# maze = input_maze(N)
# print("Maze matrix:", maze)

## Instead of writing if statements 4 times we can make a common code and loop over it 4 times:

def findPath_new(maze, n):
    all_solutions = []
    visited = [[False]*n for _ in range(n)]
    # as per DLRU
    delta_row = [+1,0,0,-1]
    delta_col = [0,-1,+1,0]
    temp_str = "DLRU"

    def generate_path(row, col, current_path, visited):
        if row == n-1 and col == n-1:
            all_solutions.append(current_path)
            return

        for i in range(n):
            next_row = row + delta_row[i] 
            next_col = col + delta_col[i]
            if next_row >= 0 and next_col >= 0 and next_row < n and next_col < n and not visited[next_row][next_col] and maze[next_row][next_col] == 1: 
                visited[row][col] = True
                generate_path(next_row, next_col, current_path+temp_str[i], visited)
                visited[row][col] = False

    if maze[0][0] == 1:
        generate_path(0, 0, "", visited)

    if not len(all_solutions): return -1
    return all_solutions

print(findPath_new(maze, n))