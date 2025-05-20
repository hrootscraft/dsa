# Problem Statement:
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 
# 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Count the number of distinct islands. An island is considered to be the same as another if 
# and only if one island can be translated (and not rotated or reflected) to equal the other.

# Example 1:

# 11000
# 11000
# 00011
# 00011

# Given the above grid map, return 1.

# Example 2:

# 11011
# 10000
# 00001
# 11011

# Given the above grid map, return 3.

# Notice that:

# 11
# 1

# and

#  1
# 11

# are considered different island shapes, because we do not consider reflection / rotation.

# Note: The length of each dimension in the given grid does not exceed 50.

# Difficulty: Medium
# Lock: Prime
# Company: Amazon, Apple, Bloomberg, Facebook, Google, Lyft, Microsoft, Uber 

## APPROACH: store the shape of the island so that when a same shape is encountered it is counted as one. 
## We store shape as a list of tuples where tuples are the subtraction of new cell from the origin cell  

def numDistinctIslands(grid):
    if not grid: return 0

    n_rows, n_cols = len(grid), len(grid[0])
    visited = set()
    shapes = set()

    # def dfs(r,c,current_shape,origin):
    #     # if the cell is out of bounds or it is visited or it is water
    #     if not (0 <= r < n_rows and 0 <= c < n_cols) or (r, c) in visited or grid[r][c] == 0:
    #         return

    #     visited.add((r, c))
    #     current_shape.add((r - origin[0], c - origin[1]))  # store position relative to the origin
    #     for dr,dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # right, bottom, left, top
    #         dfs(r+dr, c+dc, current_shape, origin)

    # for r in range(n_rows):
    #     for c in range(n_cols):
    #         if grid[r][c] == 1 and (r, c) not in visited:
    #             shape = set()
    #             dfs(r, c, shape, (r, c))
    #             shapes.add(frozenset(shape)) # convert list of positions representing the shape to tuple to make it hashable
    #             # print(shapes)
    
    def dfs_(r,c,direction):
        if not (0 <= r < n_rows and 0 <= c < n_cols) or (r, c) in visited or grid[r][c] == 0:
            return ""
        grid[r][c] = 0 # mark as visited
        path = direction
        path += dfs_(r, c+1, 'R')  # right
        path += dfs_(r+1, c, 'D')  # down
        path += dfs_(r, c-1, 'L')  # left
        path += dfs_(r-1, c, 'U')  # up
        path += 'B'  # backtrack marker
        return path
    
    for r in range(n_rows):
        for c in range(n_cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                path = dfs_(r,c,"O") # 'O' for origin
                if path: shapes.add(path)
    # print(shapes)
    return len(shapes)

grid1 = [
[1,1,0,0,0],
[1,1,0,0,0],
[0,0,0,1,1],
[0,0,0,1,1]
]

grid2 = [
[1,1,0,1,1],
[1,0,0,0,0],
[0,0,0,0,1],
[1,1,0,1,1]
]

print(numDistinctIslands(grid1))
print(numDistinctIslands(grid2))