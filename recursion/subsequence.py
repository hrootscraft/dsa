# print all subsequences (also look at bit manipulation method)
# sequences are something that follow order be it contiguous or non-contiguous; 
# eg. in "derivation", "der" or "vto" are subsequences (contiguous and non-contiguous respectively) but "dnv" or "avi" are not 
# similarly, in arr = [3,1,2], list of subsequences is [[], [3], [1], [2], [3,1], [1,2], [3,2], [3,1,2]]
# in total for n=3 sized array, there are 8 subsequences ie 2^n which includes the empty subsequence too

# the recursive method uses the intuition that for every position (0 to n-1) out of the n positions, 
# we have two options either take it in the subsequence or leave it; it being the item at that position 
# ergo the TC is O(2^n) and SC is O(n) because the depth of the recursion tree will not be more than n

def subsequences(arr):
    all_subsequences = []

    def recurse(idx, curr_subsequence):
        # if we've gone through every element in the array, 
        # add the current subsequence to the list of all subsequences
        if idx >= len(arr):
            all_subsequences.append(curr_subsequence.copy())
            return
        
        # include the current element and move to the next
        curr_subsequence.append(arr[idx])
        recurse(idx + 1, curr_subsequence)
        
        # exclude the current element and move to the next
        curr_subsequence.pop()
        recurse(idx + 1, curr_subsequence)
    # recurse(0, []) # start the recursion with an empty subsequence

    # this is faster:
    def recurse_2(idx, curr_subsequence):
        all_subsequences.append(curr_subsequence[:])
        for i in range(idx, len(arr)):
            curr_subsequence.append(arr[i])
            recurse_2(i+1, curr_subsequence)
            curr_subsequence.pop() # backtrack
    recurse_2(0,[])

    return all_subsequences
    
arr = [3,1,2]
string_1 = "BAR"
print(subsequences(arr))
print(subsequences(string_1))
