#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # approach: if you're selling on the 'i'th day then you want to buy on 
        # the day with minimum price before that 'i'th day to maximize profit
        max_profit = 0 # don't want negative profit, at the worst buy and sell on same day
        n = len(prices) 
        min_cost = prices[0]

        for i in range(1,n):
            temp_max_profit = prices[i] - min_cost
            max_profit = max(max_profit, temp_max_profit)
            min_cost = min(min_cost, prices[i])
        
        return max_profit
        
# @lc code=end

# Adobe Alibaba Amazon Apple Atlassian BlackRock Bloomberg Cisco 
# Citadel Citrix Deutsche Bank DoorDash Expedia Facebook Goldman Sachs 
# Google Grab Intel caMorgan LinkedIn Lyft Microsoft Morgan Stanley Oracle 
# Redfin SAP Snapchat Tableau Tencent Uber Visa Walmart Labs Yahoo Zillow

