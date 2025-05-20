# # divide-and-conquer algorithm : keep dividing until you hit the base condition 
# # and then start merging them in the required manner (ascending/descending)

# slowest_____________________________________________________________________________________________________
# # TC: O(n*log₂ n) where log₂ n is for the partition and merging takes n comparisons in the worst case
# # SC: O(n) algo is using indexes so constant but in merge we use a temp array which in worst case is n 
# def merge(arr, left_idx, mid_idx, right_idx): # does the merging (aka conquering) job
#     merged = []
#     left_start = left_idx # starting point for array part 1
#     right_start = mid_idx+1 # starting point for array part 2
#     while left_start <= mid_idx and right_start <= right_idx:
#         if arr[left_start] <= arr[right_start]: 
#             merged.append(arr[left_start])
#             left_start+=1
#         else:
#             merged.append(arr[right_start])
#             right_start+=1

#     merged.extend(arr[left_start:mid_idx+1])  # Append remaining elements from left subarray
#     merged.extend(arr[right_start:right_idx+1])  # Append remaining elements from right subarray

#     # make appropriate changes to arr because we're not returning the merged array here
#     for i in range(left_idx,right_idx+1):
#        arr[i] = merged[i-left_idx]
    
# def mergesort(arr, left_idx, right_idx): # does the partition job
#     # base case: if the array has one element only, we have a sorted array
#     if left_idx >= right_idx: return

#     # find the middle index to divide the array
#     mid_idx = (left_idx+right_idx)//2
#     # keep dividing the left part
#     mergesort(arr, left_idx, mid_idx) 
#     # keep dividing the right part
#     mergesort(arr, mid_idx+1, right_idx)
#     # once both left & right parts are divided into 1 element arrays, it's time to merge
#     merge(arr, left_idx, mid_idx, right_idx)

# ## driver code
# arr = [3,1,2,4,1,5,2,6,4]
# mergesort(arr, 0, len(arr)-1)
# print(arr)


# fastest_____________________________________________________________________________________________________
## TC: O(n*log₂ n) The merging step takes O(n) time, and the recursion depth is O(log n)
## SC: O(n) due to the need for auxiliary arrays during the merging step
def merge(left_arr, right_arr):
    merged = []
    left_start_idx = right_start_idx = 0
    
    # Merge the two arrays by comparing elements
    while left_start_idx < len(left_arr) and right_start_idx < len(right_arr):
        if left_arr[left_start_idx] <= right_arr[right_start_idx]:
            merged.append(left_arr[left_start_idx])
            left_start_idx += 1
        else:
            merged.append(right_arr[right_start_idx])
            right_start_idx += 1
    
    # Append remaining elements (if any) from the left and right arrays
    merged.extend(left_arr[left_start_idx:])
    merged.extend(right_arr[right_start_idx:])
    
    return merged

def mergesort(arr, left_idx, right_idx):
    if left_idx >= right_idx: 
        return arr[left_idx:right_idx+1]  # Base case: return a single-element array
    
    mid_idx = (left_idx + right_idx) // 2
    left_arr = mergesort(arr, left_idx, mid_idx)  # Recursively sort the left half
    right_arr = mergesort(arr, mid_idx + 1, right_idx)  # Recursively sort the right half
    
    # Merge the sorted left and right halves
    return merge(left_arr, right_arr)

## driver code
arr = [3,1,2,4,1,5,2,6,4]
print(mergesort(arr, 0, len(arr)-1))


# # _____________________________________________________________________________________________________
# # pythonic implementation of mergesort
# def merge(a, b, res):
#     i, j, k = 0, 0, 0 # i and j represent the starting indices of a & b arrays respectively while k is the counter to fill the result array
#     while i<len(a) and j<len(b):
#         if a[i]<b[j]:
#             res[k] = a[i]
#             i+=1
#         else:
#             res[k] = b[j]
#             j+=1
#         k+=1
            
#     res[k:] = a[i:] if i<len(a) else b[j:]
               
# def mergesort(arr):
#     if len(arr) == 1: return
#     mid = len(arr)//2
#     L = arr[:mid]
#     R = arr[mid:]
#     mergesort(L)
#     mergesort(R)
#     merge(L, R, arr)

# arr = [3,1,2,4,1,5,2,6,4]      
# mergesort(arr)
# print(arr)

