# CHERRY PICKUP II
# Problem Description: 

# We are given an ‘N*M’ matrix. Every cell of the matrix has some chocolates on it, 
# mat[i][j] gives us the number of chocolates. We have two friends ‘Alice’ and ‘Bob’. 
# Initially, Alice is standing on the cell(0,0) and Bob is standing on the cell(0, M-1). 
# Both of them can move only to the cells below them in these three directions: 
# to the bottom cell (↓), to the bottom-right cell(↘), or to the bottom-left cell(↙).

# When Alica and Bob visit a cell, they take all the chocolates from that cell with them. 
# It can happen that they visit the same cell, in that case, the chocolates need to be considered only once.

# They cannot go out of the boundary of the given matrix, we need to return 
# the "maximum" number of chocolates that Bob and Alice can together collect.

def solve(matrix):
    n_rows, n_cols = len(matrix), len(matrix[0])

    ## let alice and bob's motion through grid be represented by 'subscript' 1 & 2 respectively
    ## because we want to start the recursion at the same time and not consecutively 
    # def recurse(r1,c1, r2,c2):
    #     if r1 == n_rows-1: return matrix[r1][c1] # alice reached last row
    #     if r2 == n_rows-1: return matrix[r2][c2] # bob reached last row
    #     # but we can see that both alice and bob will anyways reach the last row at the same time because in every recursion both are moving to the same next row so instead of maintaining r1,r2 we only maintain a single r
    #     if c1<0 or c2<0 or c1>=n_cols or c2>=n_cols: return float("-inf")
    # return recurse(0,0, 0,n_cols-1) 
    
    def recurse(r,c1,c2): # TC: both alice & bob have to travel the path with n_rows and for each cell they have 3 options so (3^n)*(3^n); SC: O(n_rows) - stack space
        if c1<0 or c2<0 or c1>=n_cols or c2>=n_cols: return float("-inf") # if the cell is out of bounds you return a large negative
        
        if r == n_rows-1: # if alice & bob reach the end row
            if c1 == c2: return matrix[r][c1] # if they reach the same cell, count once
            return matrix[r][c1]+matrix[r][c2] # if they reach different cells, count both
        
        main_max = float("-inf")
        # explore all paths of alice and bob simultaneously
        # for every direction of alice, bob has 3 possible directions in the same recursion call
        # so we need to keep track of 3*3=9 possibilities; we can manually write all of them or there's a pattern:
        for i in range(-1,2): # [-1,0,1]
            for j in range(-1,2): # [-1,0,1]
                newc_1, new_c2 = c1+i, c2+j
                if c1 == c2: curr_sum = matrix[r][c1] 
                else: curr_sum = matrix[r][c1] + matrix[r][c2]
                curr_sum += recurse(r+1,newc_1,new_c2)
                main_max = max(curr_sum, main_max)
        return main_max
    
    # return recurse(0,0,n_cols-1)

    memo = {}
    def memoize(r,c1,c2):
        if (r,c1,c2) in memo: return memo[(r,c1,c2)]
        if c1<0 or c2<0 or c1>=n_cols or c2>=n_cols: return float('-inf')
        if r==n_rows-1: return matrix[r][c1] if c1==c2 else matrix[r][c1]+matrix[r][c2]
        main_max = float("-inf")
        for i in range(-1,2): 
            for j in range(-1,2): 
                new_c1, new_c2 = c1+i, c2+j
                if 0 <= new_c1 < n_cols and 0 <= new_c2 < n_cols:
                    curr_sum = matrix[r][c1] if c1 == c2 else matrix[r][c1] + matrix[r][c2]
                    main_max = max(main_max, curr_sum+memoize(r+1, new_c1, new_c2))
                    
        memo[(r,c1,c2)] = main_max
        return main_max
        
    # return memoize(0,0,n_cols-1)

    def tabulation():
        dp = [[[0]*n_cols for _ in range(n_cols)] for _ in range(n_rows)]
        # base case for n_rows-1
        for c1 in range(n_cols):
            for c2 in range(n_cols):
                if c1==c2: # if alice & bob end up at the same column
                    dp[n_rows-1][c1][c2] = matrix[n_rows-1][c1]
                else:
                    dp[n_rows-1][c1][c2] = matrix[n_rows-1][c1]+matrix[n_rows-1][c2]

        # express every state in for loops
        for r in range(n_rows-2,-1,-1):
            for c1 in range(n_cols):
                for c2 in range(n_cols):
                    
                    # copy the recursion
                    main_max = float("-inf")
                    for i in range(-1,2): # [-1,0,1]
                        for j in range(-1,2): # [-1,0,1]
                            new_c1, new_c2 = c1+i, c2+j
                            if c1 == c2: curr_sum = matrix[r][c1] 
                            else: curr_sum = matrix[r][c1] + matrix[r][c2]

                            # add the check for bounds
                            if new_c1<0 or new_c2<0 or new_c1>=n_cols or new_c2>=n_cols: curr_sum += float('-inf')
                            else:
                                curr_sum += dp[r+1][new_c1][new_c2]
                            main_max = max(curr_sum, main_max)
                    dp[r][c1][c2] = main_max

        return dp[0][0][n_cols-1]
    # return tabulation()

    def iteration(): # we saw, 1D dp was iterated using 2 variables, 2D dp used 1D array for iteration now 3D dp will use 2D for updation
        prev = [[0]*n_cols for _ in range(n_cols)]
        # base case for n_rows-1
        for c1 in range(n_cols):
            for c2 in range(n_cols):
                if c1==c2: # if alice & bob end up at the same column
                    prev[c1][c2] = matrix[n_rows-1][c1]
                else:
                    prev[c1][c2] = matrix[n_rows-1][c1]+matrix[n_rows-1][c2]

        # express every state in for loops
        for r in range(n_rows-2,-1,-1):
            temp = [[0]*n_cols for _ in range(n_cols)]
            for c1 in range(n_cols):
                for c2 in range(n_cols):
                    
                    # copy the recursion
                    main_max = float("-inf")
                    for i in range(-1,2): # [-1,0,1]
                        for j in range(-1,2): # [-1,0,1]
                            new_c1, new_c2 = c1+i, c2+j
                            if c1 == c2: curr_sum = matrix[r][c1] 
                            else: curr_sum = matrix[r][c1] + matrix[r][c2]

                            # add the check for bounds
                            if new_c1<0 or new_c2<0 or new_c1>=n_cols or new_c2>=n_cols: curr_sum += float('-inf')
                            else:
                                curr_sum += prev[new_c1][new_c2]
                            main_max = max(curr_sum, main_max)
                    temp[c1][c2] = main_max

            prev = temp
        return prev[0][n_cols-1]
    return iteration()

matrix = [
    [2, 3, 1, 2], 
    [3, 4, 2, 2], 
    [5, 6, 3, 5]
]
print(solve(matrix)) # 21