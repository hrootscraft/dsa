# Problem statement:
# You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. 
# Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.
# Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.
# For Example :
# If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exist 2 subsets with sum = 4. 
# These are {1,3} and {4}. Hence, return true.

def solve(arr,target):
    n = len(arr)

    def recurse(idx,target): # TC: O(2^n) SC: O(n)-stack space, depth of recursion
        if idx == 0: return arr[idx] == target
        if target == 0: return True # since the numbers in arr are only positive integers

        not_picked = recurse(idx-1,target)
        picked = False
        if target >= arr[idx]:
            picked = recurse(idx-1,target-arr[idx])
        return picked or not_picked

    # return recurse(n-1,target) 

    memo = {}
    def recurse_memo(idx,target): # TC: O(n*target) at max this many new problems will be solved using recursion (who's TC is significant); SC: recursion stack space + memo = O(n) + O(n*target) 
        if (idx,target) in memo: return memo[(idx,target)]
        if idx == 0: return arr[idx] == target
        if target == 0: return True # since the numbers in arr are only positive integers

        not_picked = recurse_memo(idx-1,target)
        picked = False
        if target >= arr[idx]:
            picked = recurse_memo(idx-1,target-arr[idx])
        memo[((idx,target))] = picked or not_picked
        return memo[((idx,target))]
    
    # return recurse_memo(n-1,target)

    def tabulation(): # PRO: last row and every column value will tell us whether or not a target value from 0 to target can be achieved using the n elements in the array
        dp = [[False] * (target+1) for _ in range(n)]
        if arr[0] <= target: dp[0][arr[0]] = True # check if the first element of the array can be used to make the target sum ie in the first row and col=arr[0], if arr[0]<=target then it is possible to get it in the target
        for idx in range(n): dp[idx][0] = True # base case initialization for when target is zero (first col in dp is always True because at any index if target is zero it can be added to the subset)
        
        for idx in range(1, n): # traverse from second row to the last one
            for tgt in range(1, target+1): # for each row, traverse second column to the last signifying the values in range [1,target]
                not_picked = dp[idx-1][tgt]
                picked = False
                if arr[idx] <= tgt : # check if taking the current element can be added to the subset
                    picked = dp[idx-1][tgt-arr[idx]]
                dp[idx][tgt] = picked or not_picked 
        return dp[n-1][target] # return if target can be added to the subset aka if there exists a subset with sum target
    # return tabulation() # basically, with tabulation if we find whether or not a target is achievable, we automatically get whether or not we can get targets from 1 to target in the array (check last row)

    def iteration(): # TC: O(n*target) SC: O(target) - 2 arrays of size target+1
        prev = [False]*(target+1)
        for idx in range(n): prev[0] = True 
        if arr[0] <= target: prev[arr[0]] = True

        for idx in range(1, n):
            temp = [False]*(target+1)
            temp[0] = True # first col in dp is always true
            for tgt in range(1, target+1):
                not_picked = prev[tgt]
                picked = False
                if tgt >= arr[idx]: picked = prev[tgt-arr[idx]]
                temp[tgt] = picked or not_picked
            prev = temp 
        return prev[target]
    return iteration()

arr = [1,2,3,4]
target = 37 # when target is 0, the answer will directly be true hence using recursion where sum starts from 0 and then you add current until target would be preferred but then again, 
print(solve(arr,target))