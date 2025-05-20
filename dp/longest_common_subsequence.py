# print LCS of a string # refer 1143 leetcode

# approach: create the dp table where dp[n][m] has the 
# length of the LONGEST common subsequence of string1 [0,n]
# & string2 [0,m]. we traverse this dp table as per the 
# recursion conditions: if character is same at the 2 indices
# idx1 and idx2, it comes form the previous row AND column so 
# the diagonal element, else if characters don't match, then 
# it comes from the maximum of previous row OR previous column
# and so we move the indices up to zero until we have both s1 & s2

def solve(s1,s2):
    n = len(s1)
    m = len(s2)

    def tabulation_shifted():
        dp = [[-1]*(m+1) for _ in range(n+1)]
        for idx1 in range(n+1): dp[idx1][0] = 0
        for idx2 in range(m+1): dp[0][idx2] = 0

        for idx1 in range(1,n+1):
            for idx2 in range(1,m+1):
                if s1[idx1-1] == s2[idx2-1]: dp[idx1][idx2] = 1+dp[idx1-1][idx2-1]
                else: dp[idx1][idx2] = max(dp[idx1-1][idx2],dp[idx1][idx2-1])
        return dp
    
    dp = tabulation_shifted()
    len_lcs = dp[n][m]
    lcs = "$"*len_lcs # dummy string to store answer because we'll fill it from last index to first
    idx1 = n
    idx2 = m

    while idx1>0 and idx2>0:
        if s1[idx1-1] == s2[idx2-1]:
            lcs = s1[idx1-1] + lcs[:-1]
            idx1 -= 1
            idx2 -= 1
        # when characters don't match, check which cell in the dp the len_lcs came from 
        elif dp[idx1-1][idx2] > dp[idx1][idx2-1]: # len_lcs came from previous row
            idx1 -= 1
        # when characters don't match and it came from previous column
        else:
            idx2 -= 1

    return lcs
    
s1 = "abcde"
s2 = "bdgek"
print(solve(s1,s2)) 
## TC: O(n*m) + O(n+m) ie tabulation and backtracking in while loop in the 
## worst case you backtrack all the rows and then all the columns or vice versa
## SC: O(n*m) for dp grid, stack space is eliminated