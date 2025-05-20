# binary search always implemented on a sorted space


# find the index of the target from the given array
def solve(arr, target):
    left = 0
    right = len(arr) - 1

    def iterative():
        # take two index pointers left & right to keep track of start and end of the array in consideration
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            # if the target is smaller than the mid element then search on the left side
            elif arr[mid] > target:
                right = mid - 1
            # if the target is greater than the mid element then search on the right side
            else:
                left = mid + 1
        # if target not found in the loop above then it is absent
        return -1

    # return iterative()

    def recursive():
        def bs(left, right):  # the recursive function
            # base case
            if left > right:
                return -1

            mid = (left + right) // 2
            if target == arr[mid]:
                return mid
            elif target > arr[mid]:
                return bs(mid + 1, right)
            else:
                return bs(left, mid - 1)

        return bs(0, len(arr) - 1)

    return recursive()


arr = [3, 4, 6, 7, 9, 12, 16, 17]
target = 6
print(solve(arr, target))

## TC:  O(log₂ n)
## SC:  iterative -> O(1)
##      recursive -> depth of the recursion is proportional to the height of the search space, 
##                   which is logarithmic with respect to the size of the input array so O(log₂ n)

## Overflow case: If the right is INT_MAX and there comes an instance where left and right are both at INT_MAX then calculating mid will overflow
## alternative to finding mid in that case: mid = low + (high-low)//2
