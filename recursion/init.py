# numerous function calls waiting to be implemented: segmentation fault/stack overflow
# in recursion, a function calls itself until a specific condition is met

# 1. print name 5 times
def print_name(i,n):
    if i>n: return
    print("name")
    print_name(i+1,n)
# print_name(1,5)

# 2. print linearly from 1 to n
def print_1_to_n(i,n):
    if i > n: return
    print(i)
    print_1_to_n(i+1,n)
# print_1_to_n(1,5)

# 3. print linearly from n to 1
def print_n_to_1(i,n):
    if i < 1: return
    print(i)
    print_n_to_1(i-1,n)
# print_n_to_1(5,5)
    
# 4. print linearly from 1 to n by backtracking 
def print_1_to_n_backtrack(i,n):
    if i < 1: return
    print_1_to_n_backtrack(i-1,n) # stack all solutions and then when condition is not met, backtrack
    print(i)
# print_1_to_n_backtrack(5,5)
    
# 5. print linearly from n to 1 by backtracking
# printing n to 1 would require us to fill the stack from 1 to n when it goes n+1 constraint is violated
# so we roll back and print that stack 
def print_n_to_1_backtrack(i,n):
    if i > n: return
    print_n_to_1_backtrack(i+1,n)
    print(i)
# print_n_to_1_backtrack(1,5)
    
# 6. summation of first n numbers
# goes from 10 to 1 and then when the stack is full the addition starts as elements are popped from the stack 
def sum_of_n(summ,i):
    if i<1: return summ
    summ += i
    return sum_of_n(summ,i-1)
# print(sum_of_n(0,10)) # sum of first 10 numbers

# 7a. recursion in functional programming 
def sum_of_n_(n):
    if n==0: return 0 # sum 0 nos is 0
    return n+sum_of_n_(n-1) 
# print(sum_of_n_(10))

# 7b. fibonacci
# 0 1 1 2 3 5 8 13 21 ... fib seq
# 0 1 2 3 4 5 6 7  8 ... index
def fib(n): # return nth fibonacci number
    if n <= 1: return n
    return fib(n-1)+fib(n-2) # multiple recursion calls
print(fib(8))

def fib_memo(n,memo={}):
    if n in memo: return memo[n]
    if n<= 1: return n
    memo[n] = fib_memo(n-1,memo) + fib_memo(n-2,memo)
    return memo[n]
print(fib_memo(7))

# 8. factorial (base case returns 1)
def fact(n):
    if n == 0: return 1
    return n * fact(n-1)
# print(fact(5))