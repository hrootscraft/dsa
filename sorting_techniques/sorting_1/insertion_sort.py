# takes an element and places it at the correct position
# how? takes every element from 0 to n-1 and checks with 
# every element on its left, if it is smaller it gets swapped

def insertion_sort(arr): # O(n-squared)
    n = len(arr)
    for i in range(1, n): # first element is already sorted
        key = arr[i]  # this is the element that needs to be compared with every element on its left until 0 index is reached 
        j = i-1     # start comparing with previous element
        
        # move elements greater than key ahead on the right
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            # print("swapped") # swapping never happens if the array is sorted, the best case TC would be O(n)
            
        arr[j+1] = key  # place key in correct position
        print(arr)

    return arr

print(insertion_sort([13,46,24,52,20,9]))
print(insertion_sort([1,2,3,4,5,6]))

