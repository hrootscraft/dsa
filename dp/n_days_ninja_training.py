# Problem Statement: A Ninja has an ‘N’ Day training schedule. He has to 
# perform one of these three activities (Running, Fighting Practice, or 
# Learning New Moves) each day. There are merit points associated with 
# performing an activity each day. The same activity can’t be performed 
# on two consecutive days. We need to find the maximum merit points the 
# ninja can attain in N Days.

# We are given a 2D Array POINTS of size ‘N*3’ which tells us the merit 
# point of specific activity on that particular day. Our task is to 
# calculate the maximum number of merit points that the ninja can earn.

def solve(points):
    n_days = len(points) 
    n_activites = len(points[0])

    def recurse(current_day, last_activity): # on the first call last_activity=-1 i.e. no activity was done because activities are 0,1,2
        if current_day == 0: # if we reach day 0, ie we've gotten the max points until day 1 from day n-1
            max_points = 0
            # iterate over all possible activities for day 0
            for activity in range(n_activites):
                if activity != last_activity: 
                    max_points = max(max_points, points[current_day][activity])
            return max_points 
        
        # for all days except 0, do:
        max_points = 0
        for activity in range(n_activites):
            if activity != last_activity: 
                current_day_total_points = points[current_day][activity] + recurse(current_day-1,activity)
                max_points = max(max_points, current_day_total_points)

        return max_points
    
    # return recurse(n_days-1, n_activites) # last day task done for the last day of the data we have is nothing so we represent that as 3 
    # the call means get the max points that can be earned from subset [0,n-1] given no task is done initially 
    # if recurse(2,1) is called it means get the max points from day 0 to 2 given that activity 1 was done on the previous day 3 (top down approach)
    # TC: O(n*4)*3, SC: O(n*4)

    memo = {}
    def memoization(current_day, last_activity): # there are n days and 4 activities 0,1,2,3 (3 represents no task was done) so we need a dp array of n*4 dimensions 
        if current_day == 0:
            max_points = 0
            for activity in range(n_activites):
                if activity != last_activity:
                    max_points = max(max_points, points[current_day][last_activity])
            return max_points 
        
        if (current_day, last_activity) in memo: return memo[(current_day, last_activity)]

        max_points = 0
        for activity in range(n_activites):
            if activity != last_activity: 
                current_day_total_points = points[current_day][activity] + recurse(current_day-1, activity)
                max_points = max(max_points, current_day_total_points)

        memo[(current_day, last_activity)] = max_points
        return max_points

    # return memoization(n_days-1, n_activites) # TC: O(n*4)*3 - for every point we try three posibilities at max, SC: O(n+n*4)- reduced recursion stack + memoized grid/dict

    dp = [[-1]*4 for _ in range(n_days)]
    # initialize the DP table for day 0 with base cases
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])
    def tabulation():
        for current_day in range(1, n_days): # loop through the days starting from day 1
            for last_activity in range(n_activites+1): 
                dp[current_day][last_activity] = 0  # initialize max points for current day and last activity
                for current_activity in range(n_activites):
                    if current_activity != last_activity:
                        current_day_total_points = points[current_day][current_activity] + dp[current_day-1][current_activity]
                        dp[current_day][last_activity] = max(dp[current_day][last_activity], current_day_total_points)
        return dp[n_days-1][n_activites]

    # return tabulation() # TC: O(n*4)*3, SC: O(n*4) - no stack space only dp grid space which is n*4

    def iteration(): # space optimization: how do you know when it's possible? 
        # dp[current_day][last_activity] = max(dp[current_day][last_activity], points[current_day][current_activity] + dp[current_day-1][current_activity])
        # here, we have current_day-1 in the updation step that can be taken as previous 
        # basically, when computing the next row in the dp grid, we only need the previous row values

        prev = [0]*(n_activites+1) # initialize a list to store the maximum points for each possible last activity on the previous day
        prev[0] = max(points[0][1], points[0][2])
        prev[1] = max(points[0][0], points[0][2])
        prev[2] = max(points[0][0], points[0][1])
        prev[3] = max(points[0][0], points[0][1], points[0][2])

        for current_day in range(1, n_days):
            temp = [0]*(n_activites+1)  # initialize a temporary list to store the maximum points for each possible last activity on the current day
            for last_activity in range(n_activites+1): 
                temp[last_activity] = 0 # initialize max points for current day and last activity
                for current_activity in range(n_activites):
                    if current_activity != last_activity:
                        current_day_total_points = points[current_day][current_activity] + prev[current_activity]
                        temp[last_activity] = max(temp[last_activity], current_day_total_points)
            prev = temp
        
        return prev[n_activites]

    return iteration() # TC: O(n*4)*3, SC: O(4) - array of n_activities+1 used to store only one row 

points = [  
    [10, 40, 70], # day0        
    [20, 50, 80], # day1
    [30, 60, 90]  # day2
]

print(solve(points)) # 70(Day0)+50(Day1)+90(Day2) = 210