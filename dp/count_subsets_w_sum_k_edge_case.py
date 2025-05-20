# In the problem Count Subsets with Sum K, the problem constraints stated 
# that an array element is greater than 0, so the code we have written there 
# works perfectly for the given constraints. If the constraints mentioned 
# that an array element can also be equal to 0 and the target sum can also be 0, 
# then that code will fail. To understand it we will take an example:
# Let the target arr = [0,0,1] and the target = 1.
# The previous code will give us the answer 1 as it first takes the element 
# arr[2] and then finds the answer by picking it. Then from the base condition, 
# we will return 0 ( as the target will become 0 by picking 1). But for this question, 
# the answer will be 4 with the following subsets({0,1},{0,1},{0,0,1} and {1}).

def solve(arr, k):
    n = len(arr)
    memo = {}

    def recurse_memo(idx, curr_sum): 
        if (idx,curr_sum) in memo: return memo[(idx,curr_sum)]

        if idx==0: 
            # if the target sum is 0 and the first index is also 0, 
            # like in case [0,1], we can form the subset in two ways, either 
            # by considering the first element or leaving it, so we can return 2
            if curr_sum == 0 and arr[0] == 0: return 2 

            # if target == 0, and the first element is not 0, we'll not pick the first element so just return 1 way.
            # when the first element is not 0, and the target is equal to the first element, we include it in the subset & return 1 way.
            elif curr_sum == 0 or curr_sum == arr[0]: return 1 
            return 0

        not_picked = recurse_memo(idx-1, curr_sum)
        picked = 0
        if arr[idx]<=curr_sum:
            picked = recurse_memo(idx-1, curr_sum-arr[idx])

        memo[(idx,curr_sum)] = picked+not_picked
        return memo[(idx,curr_sum)]
    return recurse_memo(n-1,k)

# arr = [1, 2, 2, 3]
# k = 3 # the sum of subset
# print(solve(arr,k)) # 3

arr = [0,0,1] 
k = 1

print(solve(arr,k)) # 4