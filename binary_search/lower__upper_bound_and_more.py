# given a sorted array of n integers and an integer x, write a program to find the lower bound of x.
# lower bound of x is the idx such that arr[idx] >= x; if any such index is not found, the lower bound algorithm returns n.
# if arr = [3, 5, 8, 15, 19, 19, 19] and x = 9 the lower bound of x is 3 ie arr[3] >= x. if x = 8 then lower bound of x is 2.
# if x = 19, then lower bound of x is 4 and if x = 22 then lower bound of x is len(arr) ie 7

# upper bound is smallest index such that arr[idx] > x. the only difference between upper and lower bound is the equal to sign.


def solve(arr, x):

    def iterative_lower():
        left = 0
        right = len(arr) - 1
        ans = right + 1

        while left <= right:
            mid = (left + right) // 2
            if (
                arr[mid] >= x
            ):  # for upper bound the only change lies here which is " if arr[mid] > x: "
                ans = mid  # possible answer if it has no lower answer towards the left side
                right = mid - 1  # change the search space to only the one on the left
            else:  # look for the lower in the right search
                left = mid + 1  # mid cannot be an answer

        return ans

    # return iterative_lower()

    def floor():
        ans = -1  # in case there is no match
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= 


arr = [3, 5, 8, 15, 19, 19]
x = 19
print(solve(arr, x))

# problem type 2: return the index of the target, if present in the array, else return the index at
# which it should be inserted in the array so as to not distort it's sorted condition
# solution: this is nothing but a problem where we would be required to find the lower bound

# problem type 3: find the floor (largest number in array <= x) and the ceil
# (smalllest number in array >= x) of given x. the array here is sorted
# solution: the ceil is nothing but lower bound element
