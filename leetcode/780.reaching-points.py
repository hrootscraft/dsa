#
# @lc app=leetcode id=780 lang=python3
#
# [780] Reaching Points
#

# @lc code=start
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # source = 2,5 & target = 19,12
        #             2,5
        #             /\
        #         7,5   2,7
        #         /\
        #    12,5  7,12
        #           /\
        #      19,12   7,19

        # memo = {}
        # def recurse(x,y):
        #     if (x,y) in memo: return memo[(x,y)]
        #     if x==tx and y==ty: return True
        #     if x>tx or y>ty: return False
        #     op1 = recurse(x,x+y)
        #     op2 = recurse(x+y,y)
        #     memo[(x,y)] = (op1 or op2)
        #     return memo[(x,y)]
        # return recurse(sx,sy) # Stack overflow!!

        # # go from target to source
        # memo = {}
        # def recurse(x,y):
        #     if (x,y) in memo: return memo[(x,y)]
        #     if x==sx and y==sy: return True
        #     if x<sx or y<sy: return False

        #     op1 = op2 = False # define op1 & op2 initially
        #     if x>y: 
        #         x = x-y # in the next iteration x will change like [19,12]-> 7,12
        #         op1 = recurse(x,y)
        #     elif y>x: 
        #         y = y-x # 7,19 -> 7,12
        #         op2 = recurse(x,y)
        #     memo[(x,y)] = (op1 or op2)
        #     return memo[(x,y)]
        # return recurse(tx,ty) # Stack overflow!!

        # we could optimize the above using modulo:
        memo = {}
        def recurse(x,y):
            if (x,y) in memo: return memo[(x,y)]
            if x==sx and y==sy: return True
            if x<sx or y<sy: return False

            op1 = op2 = False # define op1 & op2 initially
            if x>y: 
                x = x%y 
            elif y>x: 
                y = y%x 
            memo[(x,y)] = (op1 or op2)
            return memo[(x,y)]
        return recurse(tx,ty)


#  Coursera Google Quora Salesforce Twitter Uber JPMC
# @lc code=end

# https://youtu.be/tPr5Uae6Drc?si=ijXn68f17PJ9hYqS