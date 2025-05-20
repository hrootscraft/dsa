# given n return f(n) where f() is the fibonacci sequence function; 
# 0 1 1 2 3 5 8 13 ...
# 0 1 2 3 4 5 6 7  ...

import time

class Fibo:
    def __init__(self) -> None:
        self.memo = {
            0: 0,
            1: 1
        }

    ## TC: O(2^N), TC: O(2^N) where N is the depth of the tree
    def recursive(self, n): # top down approach: goes from required answer to base case
        if 0 <= n <= 1: return n
        return self.recursive(n-1)+self.recursive(n-2)

    ## TC: O(N), SC: O(N)
    def memo_recursive(self, n):
        if n not in self.memo:
            self.memo[n] = self.memo_recursive(n - 1) + self.memo_recursive(n - 2)
        return self.memo[n]

    ## TC: O(N), SC: O(N) but here, it is not the recursive stack space, it is dp array
    def tabulation(self, n): # bottom up approach: go from base case to required answer
        # init a dp array of n+1 size and make dp[0] = 0 and dp[1] = 1
        dp = [0]*(n+1)
        dp[0], dp[1] = 0, 1
        # now look at the recursive case, there n-1, n-2 from n so basically it goes from 2 to n
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    ## TC: O(N), SC: O(1)
    def iterative(self, n): 
        prev, prev_prev = 1, 0
        for _ in range(2,n+1):
            current = prev + prev_prev
            prev_prev = prev
            prev = current
        return prev
    
obj = Fibo()

start_time = time.time()
result_recursive = obj.recursive(35)
recursive_time = time.time() - start_time
print("Result of recursive function without memoization:", result_recursive)
print("Time taken for recursive function without memoization:", recursive_time)

start_time = time.time()
result_memo_recursive = obj.memo_recursive(35) # third best
memo_recursive_time = time.time() - start_time
print("\nResult of memoized recursive function:", result_memo_recursive)
print("Time taken for memoized recursive function:", memo_recursive_time)

start_time = time.time()
result_tab = obj.tabulation(35) # second best
tab_time = time.time() - start_time
print("\nResult of tabulation function:", result_tab)
print("Time taken for tabulation function:", tab_time)

start_time = time.time()
result_itr = obj.iterative(35) # fastest
itr_time = time.time() - start_time
print("\nResult of iterative function:", result_itr)
print("Time taken for iterative function:", itr_time)

## o/p:
# Result of recursive function without memoization: 9227465
# Time taken for recursive function without memoization: 1.513136386871338

# Result of memoized recursive function: 9227465
# Time taken for memoized recursive function: 1.6927719116210938e-05

# Result of tabulation function: 9227465
# Time taken for tabulation function: 9.775161743164062e-06

# Result of iterative function: 9227465
# Time taken for iterative function: 3.0994415283203125e-06