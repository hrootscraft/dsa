# given an unsorted array return the number of pairs (a,b) where a>b aka reverse pairs

class Solution:
    def mergesort(self, low, mid, high, arr) -> int:
        arr1_start = low
        arr2_start = mid+1
        merged = []
        count = 0
        while arr1_start <= mid and arr2_start <= high:
            if arr[arr1_start] > arr[arr2_start]:
                merged.append(arr[arr2_start])
                count += mid-arr1_start+1
                arr2_start += 1
            else:
                merged.append(arr[arr1_start])
                arr1_start += 1

        merged.extend(arr[arr1_start:mid+1])
        merged.extend(arr[arr2_start:high+1])

        for i in range(len(merged)):
            arr[low + i] = merged[i]

        return count

    def partition(self, low, high, arr) -> int:
        count = 0
        if low >= high: return count
        mid = (low+high)//2
        count += self.partition(low, mid, arr)
        count += self.partition(mid+1, high, arr)
        count += self.mergesort(low, mid, high, arr)
        return count
    
    def reverse_pairs(self, arr):
        return self.partition(0, len(arr)-1, arr)

sol = Solution()
print(sol.reverse_pairs([5,3,2,1,4])) # 53 52 51 54 32 31 21 therefore return 7

# during the interview you may wanna say that you're altering the array,
# but if it's not permitted you can create a copy and work on it 
# TC : O(n*log n), SC : O(n)
