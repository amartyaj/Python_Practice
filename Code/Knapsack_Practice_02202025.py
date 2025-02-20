#!/usr/bin/env python

def clean_up(num, array):
    array.sort()
    array = [x for x in array if x <= num]
    array = list(set(array))
    array.reverse()
    return array

def calc_path(amount, coins):
    def backtrack(target, start, path, result):
        if target == 0:
            result.append(path)
            return

        for i in range(start, len(coins)):
            if coins[i] > target:
                continue
            backtrack(target - coins[i], i, path + [coins[i]], result)

    start = 0
    path = []
    result = []
    backtrack(amount, start, path, result)
    return result

if __name__ == "__main__":
    N = 5
    C = [3, 2, 5, 1, 2, 8, 6, 8, 5]
    C = clean_up(N, C)
    C = calc_path(N, C)
    print(C)
