#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
from typing import *

# @lc code=start
import math

class Solution:
    def getPermutation(self, n: int, k: int):
        arr = [str(i) for i in range(1, n+1)] # list of available numbers as strings
        permutation = "" # initialize the permutation string
        k -= 1  # adjust k to be zero-based index

        for i in range(n):
            # factorial of n−1 determines the number of permutations that start with the same digit
            factorial = math.factorial(n-1-i)
            # determine the block where the digit falls into
            index = k // factorial  
            # add the digit to the permutation and remove it from the list
            permutation += arr.pop(index)
            # update k for the next iteration
            k %= factorial

        return permutation

# @lc code=end
    
## TC for above optimal code is O(n^2) because we need O(n) in the for loop and O(n) in the arr.pop()
## SC is O(n) for storing the permutation and the array of n integers

# in an interview, you'd start with 
# 1. brute force: 
        # using recursion create all the subsequences and then sort 
        # the data structure so that the solution is in lexicographical order 
        # and then select the kth element from the 1-index based data structure.
    
        #  def getPermutation(self, n: int, k: int):
        #     all_permutations = []
        #     arr = [str(i+1) for i in range(n)]

        #     def generate_permutation(idx, current_permutation):
        #         if idx >= n:
        #             all_permutations.append("".join(current_permutation))
        #             return

        #         for s in arr:
        #             if s not in current_permutation:
        #                 generate_permutation(idx+1, current_permutation + [s])

        #     generate_permutation(0, [], k)
        #     return all_permutations[k-1]  # Assuming k is 1-indexed
        
        # a) Permutation Generation: The process of generating all permutations of n numbers 
        # involves creating every possible order of those numbers. For the first position, 
        # you have n choices (any of the n numbers). For the next position, you have n-1 choices 
        # (excluding the one already used), and so on, until you have just 1 choice for the last 
        # position. This leads to a total of n! (n factorial) permutations.
        # b) Time Complexity of Generating All Permutations: The act of generating each permutation 
        # involves creating a new list (or string) from the existing one, which takes time proportional 
        # to the length of the permutation being generated. Thus, for each permutation, you're doing 
        # work proportional to n (for copying strings or lists). Therefore, the naive approach has a 
        # time complexity of O(n * n!), since for each of the n! permutations, you're performing 
        # operations that are O(n) in complexity (such as copying a list of 
        # length n or appending and then joining strings).
        # c) Selecting the k-th Permutation: After generating all permutations, selecting the k-th one 
        # is relatively trivial in terms of time complexity (O(1) if you're indexing into a list), 
        # but the heavy lifting is done by the permutation generation step.
    
        # This approach also has a significant space complexity, O(n * n!), because it stores each 
        # of the n! permutations, and each permutation is of size n.
    
# 2. optimal solution:
        # We specifically target the k-th permutation without generating all permutations 
        # and leveraging the fact that there are (n-1)! permutations that start with each digit. 
        # By calculating how many permutations to skip over, you can directly construct the k-th 
        # permutation step by step without generating the entire permutation space. 
        