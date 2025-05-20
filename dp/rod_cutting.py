# We are given a rod of size ‘N’. It can be cut into pieces. 
# Each length of a piece has a particular price given by the price array. 
# Our task is to find the maximum revenue that can be generated 
# by selling the rod after cutting (if required) into pieces.
from functools import lru_cache

price = [2,5,7,8,10] # for length 1 rod price in market is 2/-, for length 2 price is 5, 3->7,...
n = 5 # and we have a rod of length 5 which we can cut 0 to n-1 times so as to maximize the profit

# find all the combinations of the cuts to maximize profit
# lengths = [1,2,3,4,5] we can select each length any no.of times as long as it adds up to 5
# prices =  [2,5,7,8,10] this is `basically just unbounded knapsack`

def solve(price, n):

    @lru_cache(maxsize=None)
    def recurse(idx, remaining_len_rod):
        if idx==0: 
            # return (remaining_len_rod//(idx+1))*price[0] # this is basically just remaining_len_rod*price[0] because we know length of rod (idx+1) is 1 at this point
            return remaining_len_rod*price[0]

        not_cut = 0 + recurse(idx-1,remaining_len_rod)
        cut = float("-inf")
        if (idx+1)<=remaining_len_rod: # if rod length <= remaining_len_rod
            cut = price[idx] + recurse(idx,remaining_len_rod-idx-1)
        return max(cut, not_cut)
    # return recurse(n-1,n)

    def tabulation():
        dp = [[0]*(n+1) for _ in range(n)]
        for remaining_len_rod in range(n+1):
            dp[0][remaining_len_rod] = remaining_len_rod*price[0]

        for idx in range(1,n):
            for remaining_len_rod in range(n+1):
                not_cut = 0 + dp[idx-1][remaining_len_rod]
                cut = float("-inf")
                if (idx+1)<=remaining_len_rod:
                    cut = price[idx] + dp[idx][remaining_len_rod-idx-1]
                dp[idx][remaining_len_rod] = max(cut,not_cut)

        return dp[n-1][n]
    # return tabulation()

    def iteration():
        prev = [0]*(n+1)
        for remaining_len_rod in range(n+1):
            prev[remaining_len_rod] = remaining_len_rod*price[0]

        for idx in range(1,n):
            temp = [0]*(n+1)
            for remaining_len_rod in range(n+1):
                not_cut = 0 + prev[remaining_len_rod]
                cut = float("-inf")
                if (idx+1)<=remaining_len_rod:
                    cut = price[idx] + temp[remaining_len_rod-idx-1]
                temp[remaining_len_rod] = max(cut,not_cut)
            prev = temp

        return prev[n]
    # return iteration()

    def space_optimized():
        temp = [0]*(n+1)
        for remaining_len_rod in range(n+1):
            temp[remaining_len_rod] = remaining_len_rod*price[0]

        for idx in range(1,n):
            for remaining_len_rod in range(n+1):
                not_cut = 0 + temp[remaining_len_rod]
                cut = float("-inf")
                if (idx+1)<=remaining_len_rod:
                    cut = price[idx] + temp[remaining_len_rod-idx-1]
                temp[remaining_len_rod] = max(cut,not_cut)

        return temp[n]
    return space_optimized()


print(solve(price,n)) # 12