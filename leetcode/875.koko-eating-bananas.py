#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
from typing import List
import math

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # helper func
        def can_eat_all(k):
            tot_hours = sum(math.ceil(pile / k) for pile in piles) # pile/k gives the hours needed to eat a pile, we sum all such hours 
            return tot_hours <= h # if all bananas can be eaten within h, return true else false

        # we iterate k from 1 to max(piles[]); the min number for which tot_hours <= h, is our answer
        def brute_force(piles: List[int], h: int) -> int:
            for k in range(1, max(piles) + 1):
                if can_eat_all(k):  # check if koko can eat all piles at k speed within h hours
                    return k
            return max(piles)  # this line should never be reached given the constraints

        # return brute_force(piles, h) # TLE, TC: O(max(piles[])*len(piles)) 

        ## this linear search to find an answer in the range [1,max(piles[])] can be replaced by binary search
        ## as long as the answer lies in a range, binary search is going to work
        # in this problem we try k in range [1,max(piles)] 
        # let's say piles = [3,6,7,11], we try k in [1,2,3,4,...,10,11] where low=1, high=11 
        # and mid=(low+high)/2 for our BS algo. this helps us find k in O(log2 n) TC
        # we check if mid is a possible answer (using condition time<=h); because we want min k & we get a possibility at mid, we move high to left of mid
        # had we wanted max k, we'd have moved to the right. BUT, if there is an instance where time>h, then also we move to the right
        # one thing to note, initially low is always not possible, and right is always possible as per our time<=h
        # after BS algo ends, low becomes possible and high becomes not possible and so we return low as the answer. 
        # this can be observed in BS problems, we don't need to keep track of a min answer (that is initially set to INT_MAX)
        def binary_search(piles,h):
            low = 1 
            high = max(piles)

            while low<=high:
                mid = (low+high)//2
                if can_eat_all(mid): 
                    high = mid-1
                else:
                    low = mid+1

            return low
        return binary_search(piles, h) # TC: O(log2 n*len(piles)) we have replaced linear search of k with binary search ie for loop replaced with while loop

# @lc code=end

# piles = [3, 6, 7, 11]
# h = 8
# s = Solution()
# print(s.minEatingSpeed(piles, h))

