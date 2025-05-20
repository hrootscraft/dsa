#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        # number can be created by num = num*10 + current_num

        # we can 1. whitespaces 2. digits 3. a sign and 4. anything else (alphabetic characters, symbols, special characters, etc)

        # if we have whitespaces at the beginning we discard them, 
        # if it is anywhere else in the input string we return the number

        # for digits, if we have zeroes at the beginning, we discard them 
        # we read all the digits until the input ends or non-digit occurs
        # if no digit, return 0

        # there can be at most one sign char at the beginning of the string
        # or after leading whitespaces. a sign anywhere else is a non-digit char
        # and we stop building the number. if a '+' or no sign is present, num is 
        # +ve, if a '-' is the first non-whitespace char in input, num's -ve 

        # if anything else is present, we return num


        num = 0
        n = len(s)
        is_non_leading_non_char_digit = False

        def recurse(idx, is_non_leading_non_char_digit, is_negative):
            # base condition
            if idx == n-1: return num
            if not s[idx].isdigit(): pass
            if is_negative: return -num 
            else: return num

            # recursive condition
            if is_non_leading_non_char_digit: 
                return num recurse(idx+1)
# @lc code=end

