class Print_Pattern:
    def __init__(self, N) -> None:
        self.N = N

    def star_box(self):
        for _ in range(self.N):
            print("*" * self.N)

    def triangle(self):
        for i in range(self.N):
            # for _ in range(i+1):
            #     print("*",sep=" ",end="")
            print("*" * (i + 1))

    def number_triangle(self):
        for i in range(1, self.N + 1):
            for j in range(1, i + 1):
                print(j, sep=" ", end="")
            print()

    def repeated_number_triangle(self):
        for i in range(1, self.N + 1):
            for _ in range(1, i + 1):
                print(i, sep=" ", end="")
            print()

    def inverted_triangle(self):
        for i in range(self.N):
            for _ in range(self.N - i):
                print("*", sep=" ", end="")
            print()

    def inverted_number_triangle(self):
        for i in range(self.N):
            for j in range(1, self.N - i + 1):
                print(j, sep=" ", end="")
            print()

    # # In the first row (i=0) there are 4 spaces, 1 star, then again 4 spaces.
    # # In the second row (i=1) there are 3 spaces, 3 stars, then again 3 spaces
    # # so we can say that there are N-i-1 spaces, 2*i+1 stars, and then again N-i-1
    def pyramid(self):
        for i in range(self.N):
            for _ in range(self.N - i - 1):
                print(" ", sep=" ", end="")
            for _ in range(2 * i + 1):
                print("*", sep=" ", end="")
            print()

    # # In the first row (i=0) there are 0 spaces, 9 stars, then again 0 spaces.
    # # In the second row (i=1) there is 1 space, 7 stars, then again 1 space
    # # so we can say that there are i spaces, 2*N - (2*i+1) stars, and then again i space for each row
    def inverted_pyramid(self):
        for i in range(self.N):
            for _ in range(i):
                print(" ", sep=" ", end="")
            for _ in range(2 * self.N - (2 * i + 1)):
                print("*", sep=" ", end="")
            print()

    # For N=3 we have 5 rows, and for N=6 we have 11 rows, hence the outer loop will run for 2*N-1 times.
    # For the inner loop where we print the stars if row no. is less than or equal to N, then the stars which
    # are printed in each row are equal to the row index itself. But, when i becomes more than N, the no. of stars
    # decrease by 1 with each increasing row. Therefore, stars printed would be 2*N-i after i becomes greater than N.
    def side_triangle(self):
        for i in range(1, 2 * self.N):
            if i <= self.N:
                stars = i
            else:
                stars = 2 * self.N - i

            for _ in range(stars):
                print("*", sep=" ", end="")
            print()

    def zero_one_traingle(self):
        # # Logic 1: if the row and column index add up to an even number then print 1 and if is odd then print 0
        # for i in range(1, self.N + 1):
        #     for j in range(1, i + 1):
        #         if (i + j) % 2 == 0:
        #             print("1", sep=" ", end="")
        #         else:
        #             print("0", sep=" ", end="")
        #     print()

        # Logic 2: print binary digits alternatively and change the start as per row index
        for i in range(1, self.N + 1):
            if i % 2 == 0:
                start = 0
            else:
                start = 1
            for j in range(1, i + 1):
                print(start, sep=" ", end="")
                start = 1 - start
            print()

    def two_traingles(self):
        for i in range(1, self.N + 1):
            for j in range(1, i + 1):
                print(j, sep=" ", end="")
            for _ in range(2 * self.N - i * 2):
                print(" ", sep=" ", end="")
            for j in range(i, 0, -1):
                print(j, sep=" ", end="")
            print()

    def numbered_triangle(self):
        n = 1
        for i in range(self.N):
            for _ in range(i + 1):
                print(n, sep=" ", end="")
                n += 1
            print()

    def alphabet_traingle(self):
        for i in range(1, self.N + 1):
            for j in range(i):
                print(chr(65 + j), sep=" ", end="")
            print()

    def inverted_alphabet_traingle(self):
        for i in range(self.N, 0, -1):
            for j in range(i):
                print(chr(65 + j), sep=" ", end="")
            print()

    def repeated_alphabet_traingle(self):
        for i in range(1, self.N + 1):
            for j in range(i):
                print(chr(64 + i), sep=" ", end="")
            print()

    def alphabet_pyramid(self):
        for i in range(1, self.N + 1):
            for j in range(self.N - i):
                print(" ", sep=" ", end="")
            for j in range(i):
                print(chr(65 + j), sep=" ", end="")
            for j in range(i - 2, -1, -1):
                print(chr(65 + j), sep=" ", end="")
            print()

        # # pythonic approach
        # for i in range(self.N):
        #     left_part = ''.join(chr(65 + j) for j in range(i + 1))
        #     right_part = left_part[-2::-1]
        #     row = left_part + right_part
        #     print(row.center(2 * self.N - 1))
        #     # print(row.rjust(2 * self.N - 1))
        #     # print(row.ljust(2 * self.N - 1))

    def reverse_alphabet_triangle(self):
        for i in range(1, self.N + 1):
            for j in range(self.N - i, self.N):
                print(chr(65 + j), end="", sep=" ")
            print()

    def boxed_diamond(self):
        init_space = 0
        for i in range(self.N):
            for j in range(self.N - i):
                print("*", sep=" ", end="")
            for j in range(init_space):
                print(" ", sep=" ", end="")
            for j in range(self.N - i):
                print("*", sep=" ", end="")
            init_space += 2
            print()

        init_space = self.N * 2 - 2
        for i in range(1, self.N + 1):
            for j in range(i):
                print("*", sep=" ", end="")
            for j in range(init_space):
                print(" ", sep=" ", end="")
            for j in range(i):
                print("*", sep=" ", end="")

            init_space -= 2
            print()

    def butterfly(self):
        # there's no horizontal symmetry 'cause of one line only,
        # so we take outer loop to print 2*N-1 lines and add a condition
        # for varying spaces going top to bottom. when n=5

        #   row star space star
        #   1      1   8   1
        #   2      2   6   2
        #   3      3   4   3
        #   4      4   2   4
        #   5      5   0   5
        #   6      4   2   4
        #   7      3   4   3
        #   8      2   6   2
        #   9      1   8   1
        init_space = self.N * 2
        for i in range(1, 2 * self.N):
            if i > self.N:
                stars = 2 * self.N - i
                init_space += 2
            else:
                stars = i
                init_space -= 2

            for j in range(stars):
                print("*", sep=" ", end="")

            for j in range(init_space):
                print(" ", sep=" ", end="")

            for j in range(stars):
                print("*", sep=" ", end="")
            print()

    def empty_rectangle(self):
        #   00  01  02  03
        #   10  11  12  13
        #   20  21  22  23
        #   30  31  32  33
        # print stars on the boundaries
        for i in range(self.N):
            for j in range(self.N):
                if i == 0 or i == self.N - 1 or j == 0 or j == self.N - 1:
                    print("*", sep=" ", end="")
                else:
                    print(" ", sep=" ", end="")
            print()

    def reverse_digit_box(self):
        # 3 3 3 3 3                                     0 0 0 0 0
        # 3 2 2 2 3                                     0 1 1 1 0
        # 3 2 1 2 3 convert this into another matrix -> 0 1 2 1 0
        # 3 2 2 2 3                                     0 1 1 1 0
        # 3 3 3 3 3                                     0 0 0 0 0
        # so this is N - current_matrix = new_matrix
        # outer loop runs for 2*n-1 times and so does the inner one
        for i in range(self.N * 2 - 1):
            for j in range(self.N * 2 - 1):
                dist_top = i
                dist_bottom = self.N * 2 - 1 -1 - i
                dist_left = j
                dist_right = self.N * 2 - 1 -1 - j
                current_val = min(dist_top, dist_bottom, dist_left, dist_right)
                print(current_val, sep=" ", end="")
            print()

N = 5
p = Print_Pattern(N)
p.star_box()
# p.triangle()
# p.number_triangle()
# p.repeated_number_triangle()
# p.inverted_triangle()
# p.inverted_number_triangle()
# p.pyramid()
# p.inverted_pyramid()
# p.side_triangle()
# p.zero_one_traingle()
# p.two_traingles()
# p.numbered_triangle()
# p.alphabet_traingle()
# p.inverted_alphabet_traingle()
# p.repeated_alphabet_traingle()
# p.alphabet_pyramid()
# p.reverse_alphabet_triangle()
# p.boxed_diamond()
# p.butterfly()
# p.empty_rectangle()
# p.reverse_digit_box()
