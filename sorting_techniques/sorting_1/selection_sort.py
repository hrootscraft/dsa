# what do we select? minimum AND then swap that minimum with the 
# first element of remaining unsorted array to eventually get a sorted array. 
# eg.   [7 4 0 1 3]  
#    -> [0 4 7 1 3] swap happened b/w 0 and min_idx in unsorted array [0,n-1]
#    -> [0 1 7 4 3] swap happened b/w 1 and min_idx in unsorted array [1,n-1]
#    -> [0 1 3 4 7] swap happened b/w 2 and min_idx in unsorted array [2,n-1]  
# and the check happens twice again for [3,n-1] and [4,n-1] where n=5 

def selection_sort(arr): # O(n-squared)
    n = len(arr)
    for i in range(n-1): # pointer representing the start of unsorted array will go from 0 to n-2 (not n-1 because an array with 1 element is always sorted)
        min_idx = i # initially consider the element at i as the minimum for every unsorted array going from i to n-1
        for j in range(i,n): # j will specify the range of the unsorted arrays, it goes from j to n-1
            if arr[j] < arr[min_idx]: min_idx = j
        # after the above for loop we have the min_idx, now we swap start of the subarray and min 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # print(arr)
    return arr

# print(selection_sort([7,4,0,1,3]))
print(selection_sort([13,46,24,52,20,9]))
            


