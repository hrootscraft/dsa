import math

def solve(n):

    def extract_digits(n):
        temp = n
        while temp:
            last_digit = temp % 10
            print(last_digit)
            temp = temp // 10 

    # return extract_digits(n)

    def n_digits(n):
        # temp = n
        # count = 0
        # while temp:
        #     last_digit = temp % 10
        #     count += 1
        #     temp = temp // 10 
        # return count

        return int(math.log10(n)+1)

    return n_digits(n) # TC of both methods is O( log10(n) ) because it's getting divided by 10 approx log10(n) times

    def reversed(n):
        rev_num = 0
        temp = n
        while temp:
            last_digit = temp % 10
            print(last_digit)
            temp = temp // 10 
        


print(solve(729))