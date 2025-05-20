board = [
    [1,2,3,4,13,16],
    [5,6,7,8,14,17],
    [9,10,11,12,15,18],
    [19,20,21,22,23,24],
    [25,26,27,28,29,30],
    [31,32,33,34,35,36]
]

rows = len(board) # 3
cols = len(board[0]) # 5
tot = rows*cols
grid_dim_r = 2
grid_dim_c = 3

# Calculate the number of grids per dimension
num_grids_row = rows // grid_dim_r  # How many grids fit vertically
num_grids_col = cols // grid_dim_c  # How many grids fit horizontally

# assume we have smaller grids in here of the dimension 2x3 (dim_rxdim_c)
# we want to print each small grid using a single iterable i (this logic is used in sudoku-solver)
# then we can say that we have two broad level columns (c0,c1) and 3 broad level rows (r0,r1,r2)
# we want to now print the grid represented by 
# r0xc0 - [[1,2,3],[5,6,7]], r0xc1 - [[4,13,16],[8,14,17]]
# r1xc0 - , r1xc1 - 
# r2xc0 - , r2xc1 - 

def print_grids():
    for r in range(rows):
        for c in range(cols):
            # Calculate which grid (r, c) belongs to
            grid_r = r // grid_dim_r
            grid_c = c // grid_dim_c
            print(f"board[{r}][{c}]={board[r][c]} belongs to grid [{grid_r}][{grid_c}]")

print_grids()