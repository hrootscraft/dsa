def find_substrings(s):
    substrings = []
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.append(s[i:j])
    return substrings

string = "abcd"
all_substrings = find_substrings(string)
print("All substrings of '{}' are: {}".format(string, all_substrings))
