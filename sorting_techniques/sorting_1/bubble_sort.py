# pushes the maximum to the last by adjacent swaps
# the unsorted array comes to the left here and the sorted part goes on the right

def bubble_sort(arr): # O(n-squared): this can be optimized if in the first outer loop there is no swapping any time then the array is already sorted and we don't need to check for further subarrays
    n = len(arr)
    for i in range(n-1, 0, -1): # i records the last index of the array to be considered, it should go from n-1 to 1
        for j in range(i): # j should go from 0 to i-1
            if arr[j] > arr[j+1]: arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)

    return arr

def optimized_bubble_sort(arr): # in the best case this (outer loop) will run only once giving O(n) TC
    n = len(arr)
    for i in range(n-1, 0, -1): # i records the last index of the array to be considered, it should go from n-1 to 1
        is_swapped = False
        for j in range(i): # j should go from 0 to i-1
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_swapped = True
        print(arr)
        if not is_swapped: break # break if no swaps occurred (array is sorted)

    return arr


# print(bubble_sort([13,46,24,52,20,9]))
print(optimized_bubble_sort([13, 46, 24, 52, 20, 9]))
print()
print(optimized_bubble_sort([1,2,3,4,5,6]))


