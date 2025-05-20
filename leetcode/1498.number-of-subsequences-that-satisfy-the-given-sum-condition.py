#
# @lc app=leetcode id=1498 lang=python3
#
# [1498] Number of Subsequences That Satisfy the Given Sum Condition
#
from typing import List
# @lc code=start
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ## 3. 2-pointer method : TC-O(n*log n) SC-O(n)
        nums.sort()
        n = len(nums)
        start, end = 0, n-1
        count = 0
        dp = [1]*n
        MOD = 10 ** 9 + 7

        # MOD operation ensures that the values stored in the dp array remain within a certain range to 
        # avoid integer overflow. Taking the modulo helps keep the values manageable 
        # and prevents them from becoming too large.

        # The reason for using (dp[i−1]×2)mod  MOD(dp[i−1]×2)modMOD instead of pow(dp[i−1],2)pow(dp[i−1],2) 
        # lies in efficiency and optimization. Exponentiation operations, especially involving large integers, 
        # can be computationally expensive compared to simple multiplication.
        for i in range(1,n):
            # number of subsequences with n elements is 2^n
            dp[i] = (dp[i-1]*2) % MOD 

        while start <= end:
            if nums[start] + nums[end] <= target: 
                count = (count + dp[end-start]) % MOD
                start+=1
            else: end-=1
        
        return count


        # ## 2. modified recursion # still TLE error!! :( will have to resort to DP even though initial cases passed
        # # this pattern of using left and right is used when we want to return a single output
        # n = len(nums)
        # def subseq_recurse(idx: int, arr: List[int]) -> int:
        #     if idx >= n :
        #         if arr and min(arr) + max(arr) <= target: return 1
        #         return 0
        #     arr.append(nums[idx])
        #     left = subseq_recurse(idx+1, arr)
        #     arr.pop()
        #     right = subseq_recurse(idx+1, arr)
        #     return left+right
        # return subseq_recurse(0, [])
    
        # ## 1.recursion # time limit exceeds because we're exploring all the possible subsequences (initial 3 cases passed)
        # n = len(nums)
        # no_of_req_subseq = 0

        # def subseq_recurse(idx, arr):
        #     nonlocal no_of_req_subseq
        #     if idx >= n :
        #         if arr and min(arr) + max(arr) <= target: no_of_req_subseq += 1
        #         return
        #     arr.append(nums[idx])
        #     subseq_recurse(idx+1, arr)
        #     arr.pop()
        #     subseq_recurse(idx+1, arr)
        #     return
        # subseq_recurse(0, [])
        # return no_of_req_subseq


        # ## NOTE_ : In recursion there's another type, where you are required to return 
        # # the first value that satisfies the given condition and recurse no more. 
        # # The pattern for this kinda problem would be like so and the return type of recursive function would be bool 
        # # (here, we'll return any subsequence that satisfies the given condition)
        # n = len(nums)
        # one_subseq_that_satisfied_cond = []
        # def subseq_recurse(idx: int, arr: List[int]) -> bool:
        #     nonlocal one_subseq_that_satisfied_cond
        #     if idx >= n:
        #         # condition satisfied then return true
        #         if arr and min(arr) + max(arr) <= target: 
        #             one_subseq_that_satisfied_cond = arr
        #             return True
        #         # condition not satisfied
        #         return False
        #     arr.append(nums[idx])
        #     # when you have an answer (any 1 answer) return and break the recursion
        #     if(subseq_recurse(idx+1, arr)): return True
        #     arr.pop()
        #     if(subseq_recurse(idx+1, arr)): return True
        #     return False 
        # subseq_recurse(0,[])
        # print(one_subseq_that_satisfied_cond)
# @lc code=end

