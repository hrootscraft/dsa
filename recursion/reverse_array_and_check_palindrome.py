class Reverse:
    def __init__(self, arr) -> None:
        self.arr = arr
        self.len_arr = len(arr)

    def __str__(self,arr=None) -> str:
        arr_to_print = arr if arr is not None else self.arr
        for item in arr_to_print:
            print(item, end=" ")
        print()

    @staticmethod
    def swap(arr, s,e) -> None:
        arr[s], arr[e] = arr[e], arr[s]

    def w_two_pointer(self) -> None:
        arr_copy = self.arr.copy()
        start = 0
        end = len(arr_copy)-1
        while(start<end):
            self.swap(arr_copy, start, end)
            start += 1
            end -= 1
        self.__str__(arr_copy)

    def w_one_pointer(self) -> None:
        arr_copy = self.arr.copy()
        i = 0
        n = len(arr_copy)
        while(i<n/2):
            self.swap(arr_copy, i, n-i-1)
            i += 1
        self.__str__(arr_copy)

    def w_recursion_two_pointer(self) -> None:
        arr_copy = self.arr.copy()
        start = 0
        end = self.len_arr - 1

        def rec(start,end,arr):
            # base condition
            if start>=end: 
                return 
            self.swap(arr, start, end) # operation
            rec(start+1,end-1,arr) # recursive call

        rec(start, end, arr_copy)
        self.__str__(arr_copy)

    def w_recursion_one_pointer(self) -> None:
        arr_copy = self.arr.copy()
        i = 0
        n = len(arr_copy)

        def rec(i,arr):
            # base condition
            if i>=n/2: 
                return 
            self.swap(arr, i, n-i-1) # operation
            rec(i+1,arr) # recursive call

        rec(i, arr_copy)
        self.__str__(arr_copy)

    def if_str_palindrome_iterative(self,s, n) -> bool:
        s = s.lower()
        for idx in range(len(s)//2):
            if s[idx] != s[n-idx-1]: return False
            return True

    def if_str_palindrome_rec(self,s,n,i) -> bool:
        if i>n/2: return True
        if s[i] != s[n-i-1]: return False
        return self.if_str_palindrome_rec(s,n,i+1)

    def if_str_palindrome_slicing(self,s) -> bool:
        s = s.lower()
        return s == s[::-1]

## driver code
arr = [2,5,7,9,3,1]
string_1 = "Rutuja"
string_2 = "Level"
r = Reverse(arr)
# r.w_two_pointer()
# r.w_one_pointer()
# r.w_recursion_two_pointer()
# r.w_recursion_one_pointer()
# print(f"{string_1}", r.if_str_palindrome_iterative(string_1, len(string_1)))
# print(f"{string_2}", r.if_str_palindrome_iterative(string_2, len(string_2)))
print(f"{string_1}", r.if_str_palindrome_rec(string_1.lower(), len(string_1), 0))
print(f"{string_2}", r.if_str_palindrome_rec(string_2.lower(), len(string_2), 0))
# print(f"{string_1}", r.if_str_palindrome_slicing(string_1,))
# print(f"{string_2}", r.if_str_palindrome_slicing(string_2,))