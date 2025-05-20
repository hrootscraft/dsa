# print subsequences whose sum is k
# parameters we can track: the index, the subsequence, and the sum
from typing import List

## TYPE 1: Get all subsequences satisfying the given condition
def subseq_satisfying_condition(arr: List[int], k: int) -> List[List[int]]:
    n = len(arr)
    all_subsequences = []

    def subseq(idx: int, current_subsequence: List[int], current_sum: int) -> None:
        if idx >= n :
            if current_sum == k: 
                all_subsequences.append(current_subsequence[:])
            return
        
        # current_subsequence.append(arr[idx])
        # current_sum += arr[idx]
        # subseq(idx+1, current_subsequence, current_sum)

        # current_subsequence.pop()
        # current_sum -= arr[idx]
        # subseq(idx+1, current_subsequence, current_sum)

        ## shorter version of above snippet:
        # include the current element
        subseq(idx+1, current_subsequence+[arr[idx]], current_sum+arr[idx])
        # exclude the current element
        subseq(idx+1, current_subsequence, current_sum)


    subseq(0, [], 0)
    return all_subsequences

print(subseq_satisfying_condition([1,2,1], 2))

## TYPE 2: Get any 1 subsequence satisfying the given condition
# we can surely use a flag which is set when get the first sequence is gotten and then when we check for the flag i returns 
# but we can use a more mature method here; we use the return from the base condition ie track if it's true or false
# if the base condition is true ie we have a subsequence that satisfied the given condition we no longer execute the subsequent recursive calls

def one_subseq_satisfying_condition(arr: List[int], k: int) -> List[List[int]]:
    n = len(arr)
    all_subsequences = []

    def subseq(idx: int, current_subsequence: List[int], current_sum: int) -> bool:
        # base condition
        if idx >= n :
            # sum condition satisfied
            if current_sum == k: 
                all_subsequences.append(current_subsequence[:])
                return True
            # sum condition not satisfied
            return False

        # if adding the element recursive call returns True, there is no need to execute the next call hence we return True here
        if subseq(idx+1, current_subsequence+[arr[idx]], current_sum+arr[idx]) == True: return True
        # similar check is done below
        if subseq(idx+1, current_subsequence, current_sum) == True: return True

        # if none of the above returns true then return false 
        return False

    subseq(0, [], 0)
    return all_subsequences

print(one_subseq_satisfying_condition([1,2,1], 3))

## TYPE 3: Get the count of all subsequences satisfying the given condition
# no need of submitting the list of subsequences, we just need to track the count
# we do this by having the base condition return the count so that the recursive function returns the count
# also, here we do not need to track current_subsequence we've been tracking so far only the current_sum would suffice
def count_subseq_satisfying_condition(arr: List[int], k: int) -> int:
    n = len(arr)
    def subseq(idx: int, current_sum: int) -> int:
        # if the base condition is satisfied ie we have a subsequence satisfying given condition, 
        # we return 1 meaning we have found 1 subsequence
        if idx >= n:
            # sum condition satisfied
            if current_sum == k:
                return 1
            # sum condition not satisfied
            return 0
        
        # we can add another base condition if we get current_sum>k, 
        # then we can never get a sum less than k even in further 
        # recursion calls assuming the array contains all positive number
        # else if there's negatives too in the array, there's no use of this base condition
        if current_sum > k: return 0

        left_tree = subseq(idx+1, current_sum+arr[idx])
        right_tree = subseq(idx+1, current_sum)
        
        return left_tree+right_tree

    return subseq(0, 0)

print(count_subseq_satisfying_condition([1,2,1], 2))

# in the above function we have only 2 recursion calls, sometimes we might need n recursive calls
# in that case, we set a sum variable to track it like so:
# s=0
# for (i=1 -> n)
#   s+=f()
# return s
# This pattern is observed in N-Queens
