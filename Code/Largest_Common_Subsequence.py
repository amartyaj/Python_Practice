#!/usr/bin/env python3


import pprint as p


def find_largest_subsequence(*args):
    pass

    result = ""
    s1 = args[0]
    s2 = args[1]

    m = len(s1)
    n = len(s2)
    # print(m, n)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # print(dp)
    max_length = 0
    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i

    # p.pp(dp)
    result = s1[end_index - max_length : end_index]
    return result


if __name__ == "__main__":
    pass

    string1 = ["asdfghjkl", "asdvvvbbbnn", "eeerrrggghh", "qwerty"]
    string2 = ["dfghj", "vvvxbbbynn", "aaeeerrrggghhgg", "qwerxty"]

    for first_string, second_string in zip(string1, string2):
        largest_subsequence = find_largest_subsequence(first_string, second_string)

        print("\n", end="")
        print(f"String1: {first_string}")
        print(f"String2: {second_string}")
        print(f"Largest substring: {largest_subsequence}")
