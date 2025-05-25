# divide and merge; see implementation from recursion folder too


def merge(arr1, arr2):
    merged = []
    p1, p2 = 0, 0  # p1 and p2 track start of arrays
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            merged.append(arr1[p1])
            p1 += 1
        else:
            merged.append(arr2[p2])
            p2 += 1

    while p1 < len(arr1):  # append remaining elements of arr1 if any
        merged.append(arr1[p1])
        p1 += 1
    while p2 < len(arr2):  # append remaining elements of arr2 if any
        merged.append(arr2[p2])
        p2 += 1

    return merged


def divide(arr):
    if len(arr) <= 1:
        return arr  # 1 element array or 0 element is always sorted
    mid = len(arr) // 2

    # divide arrays into two halves
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # recursively sort both halves
    left_arr = divide(left_arr)
    right_arr = divide(right_arr)

    # merge the sorted halves
    return merge(left_arr, right_arr)


arr = [4, 2, 1, 6, 7]
print(divide(arr))
