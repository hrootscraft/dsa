# return the minimum no.of operations to convert string s1 to s2
# refer 1143 leetcode; this also the exact solution for 583 leetcode 
# to find the minimum no.of deletions to make s1 & s2 same
def solve(s1,s2):
    n = len(s1)
    m = len(s2)

    def iteration_shifted(): ## TC: O(n*m) two nested loops, SC: O(m) for arrays
        prev = [0]*(m+1)
        for idx1 in range(1,n+1):
            temp = [0]*(m+1)
            for idx2 in range(1,m+1):
                if s1[idx1-1] == s2[idx2-1]: 
                    temp[idx2] = 1+prev[idx2-1]
                else:
                    temp[idx2] = max(prev[idx2],temp[idx2-1])
            prev = temp
        return prev[m]    
    
    lcs = iteration_shifted()
    return n+m-2*lcs

s1 = "abcd"
s2 = "anc"

print(solve(s1,s2))

# it is always possible to change s1 to s2: in the worst case we'd need 
# n insertions and m deletions so n+m operations where n & m are 
# lengths of strings s1 & s2.