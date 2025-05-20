#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#

# asked in Apple, Meta, Google, LinkedIn, Microsoft, Snapchat

# "123" 1+2+3 ✓ 12+3 ✓ 1+23 ✓ 32+1 ✓ 21+3 ✓
# "105" 01+5 X 05+1 X in case of leading zeroes we need to force it to go to the next number 

from typing import List
# @lc code=start
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        all_expressions = []
        
        def generate_expression(idx, curr_expression, curr_value, prev_num): 
            # we need the previous number tracked because when we have "1+2|*3" as per curr_value it would be 3*3=9
            # but actually, it should be (previous number)*(current number) ie 1+2*3=7 
            if idx >= len(num):
                if curr_value == target:
                    all_expressions.append("".join(curr_expression))
                return 

            # loop through the remaining characters in the string num
            for i in range(idx, len(num)):
                if i != idx and num[idx] == '0':
                    break  # avoid leading zeros

                curr_str = num[idx:i+1]
                curr_num = int(curr_str)

                if idx == 0: # when the current expression is empty 
                    generate_expression(i+1, [curr_str], curr_num, curr_num)
                else:
                    generate_expression(i+1, curr_expression+["+", curr_str], curr_value+curr_num, curr_num)
                    generate_expression(i+1, curr_expression+["-", curr_str], curr_value-curr_num, -curr_num)
                    generate_expression(i+1, curr_expression+["*", curr_str], curr_value-prev_num+curr_num*prev_num, curr_num*prev_num)
        
        generate_expression(0, [], 0, 0)
        return all_expressions
    
# @lc code=end
    
# Time Complexity:

#   Backtracking: The main work is done by the backtrack function, which explores all possible 
#   combinations of operators and operands. The number of recursive calls depends on the length 
#   of the input string num. For each position in the string, we explore three possibilities 
#   (addition, subtraction, and multiplication) and there is a 4th one which is implicit where 
#   we skip operator and take another digit (eg. we go 1+2, 1-2, 1*2, 12), leading to a time  
#   complexity of approximately O(4^N), where N is the length of the input string.

#   Appending to Result: Appending to the result list involves joining the elements, 
#   which takes O(N) time for each expression. Since there could be up to 
#   O(4^N) valid expressions, the total time complexity becomes O(N * 4^N).

# Space Complexity:

#   Recursive Stack: The space complexity is dominated by the recursive calls. At any point, 
#   the maximum depth of recursion is limited by the length of the input string num, leading 
#   to a space complexity of O(N), where N is the length of the input string.
#   Result List: The space complexity of the result list (all_expressions) is proportional 
#   to the number of valid expressions generated. In the worst case, where all combinations 
#   are valid, the space complexity would be O(4^N), but typically it would be less than that.

