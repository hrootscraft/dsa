# problem: print all subsequences 
# can also be done using recursion but here we use power set
# if len of string is n then the # of substrings will be 2^(n) similar for array
# in this list of substrings, the empty substring is also included

# binary representation of 5 is bin_rep=101, now we want to check if "i"th bit in this bin_rep is set or not
# we achieve this by using & operation with a number that contains 1 at the "i"th position and zeroes after it
# if the & operation of bin_rep and this new number (lso) is not zero then it is set, else it is not set
# lso is obtained using left shift operator 1<<i ie lso=1<<i and now we check bin_rep&lso==0

#   a   b   c -> string
#   0   1   2 -> idx in array/string

# for eg. we know the # of subsequences is 8, so we write the binary representation of nos. 0 to 7
#   |   2   1   0   -> idx in bit representation
# __|_______________
# 0 |   0   0   0   ->  ""      Here, 1->pick and 0->not pick
# 1 |   0   0   1   ->  "a"
# 2 |   0   1   0   ->  "b"
# 3 |   0   1   1   ->  "ab"
# 4 |   1   0   0   ->  "c"
# 5 |   1   0   1   ->  "ac"
# 6 |   1   1   0   ->  "bc"
# 7 |   1   1   1   ->  "abc"

## pseudocode:
# 1. generate these bit representations from 0 to 2^(n)-1 where n is the length of the string (the # of bits is also n)
# 2. for each generated binary representation, select those indices from the string which are set in the binary representation

# def subsequences(s, result=[]):
#     # if isinstance(s, list):
#     #     s = ''.join(map(str, s))  # convert the list of numbers to a string
#     n = len(s)
#     total_subsequences = 1 << n # returns 2^n
#     for num in range(total_subsequences):
#         subsequence = ""
#         # check each bit of the current number 'num'
#         for i in range(n):
#             # if "i"th bit of num is set, include the corresponding character from 's'
#             if (num & (1 << i)) > 0:
#                 subsequence += s[i]
#         result.append(subsequence)
#     return result

# here, the TC is 2^(n) * n and SC is O(1)
# whereas, in recursion the TC is 2^n [n->size of array or string] and SC is O(n)
# this method is more efficient than recursion

def subsequences(s):
    result=[]
    if isinstance(s, list): # if s is an instance of list
        n = len(s)
        total_subsequences = 1 << n  # returns 2^n
        for num in range(total_subsequences):
            subsequence = []
            # check each bit of the current number 'num'
            for i in range(n):
                # if "i"th bit of num is set, include the corresponding element from 's'
                if (num & (1 << i)) > 0:
                    subsequence.append(s[i]) # the only difference between list and string
            result.append(subsequence)
    else: # if s is an instance of string 
        n = len(s)
        total_subsequences = 1 << n  # returns 2^n
        for num in range(total_subsequences):
            subsequence = ""
            # check each bit of the current number 'num'
            for i in range(n):
                # if "i"th bit of num is set, include the corresponding character from 's'
                if (num & (1 << i)) > 0:
                    subsequence += s[i]
            result.append(subsequence)
    
    return result

## driver code
string_1 = "abc"
print(subsequences(string_1))

arr = [3,1,2]
print(subsequences(arr))