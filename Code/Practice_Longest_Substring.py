#!/usr/bin/env python3


import pprint as p


def find_longest_substr(*args):
    pass

    s1 = args[0]
    s2 = args[1]

    m = len(s1)
    n = len(s2)

    max_len = 0
    end_idx = 0

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_idx = i

    # print("")
    # p.pp(dp)
    result = s1[end_idx - max_len : end_idx]
    return result


if __name__ == "__main__":
    pass

    string1 = ["aaa", "asdfghjkl", "bbb", "bqwertxy", "bqwertyxyzxc"]
    string2 = ["aaaa", "asdfghxjkl", "bb", "qwerty", "qwertyyxzy"]

    for i, j in zip(string1, string2):
        longest_substr = find_longest_substr(i, j)
        print(longest_substr)
