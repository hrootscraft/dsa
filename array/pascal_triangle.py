# Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.
# Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.
# Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.


## TC: O(C) where C is the column number because we are running the loop for r times and r=C-1
## SC: O(1) no extra space required 
def v1(R,C): # R,C are 1-indexed
    # we can use nCr formula to find the element in Pascal's Triangle at (R,C) where n=R-1 and r=C-1
    # nCr = n! / [r! * (n-r)!] = n*(n-1)*(n-2)*...*(n-r+1) / r*(r-1)*(r-2)*...*1 = (n/1) * ((n-1)/2) *...* ((n-r+1)/r) 
    n = R-1
    r = C-1
    res = 1
    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)

    return res

# print(v1(5,3)) # 6


## TC: O(N*C) 
## SC: O(N) space required scales linearly with the input NN
def v2(N): # N is 1-indexed
    # for every column 1 to N and row N, we find the element at (R,C) and get that row
    res = []
    for C in range(1,N+1):
        res.append(v1(N,C)) 
    return res

# print(v2(5)) # [1, 4, 6, 4, 1]
 

## TC: O(N) above quadratic time is now made linear
## SC: O(N)
def optimal_v2(N): # N is the row number
    res = [1]
    num = 1 # num is the first element in res, using num we calculate consequent elements in that row N
    for c in range(1,N): # iterate columns no.of times where # of columns = N
        num = num*(N-c)
        num = num//c
        res.append(num)
    return res

# print(optimal_v2(5))

## TC: O(N*N*C) in the worst case this is approx cubic time
## SC: O(N*N) each row has N elements and there are N rows
def v3(n_rows):
    grid = []
    for R in range(1,n_rows+1):
        grid.append(v2(R))  
    return grid

# print(v3(5)) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

def optimal_v3(n_rows): # this only used optimal_v2 which makes it TC quadratic which is the optimal solution 
    grid = []
    for R in range(1,n_rows+1):
        grid.append(optimal_v2(R))
    return grid

print(optimal_v3(5))