#!/usr/bin/env python


def clean_up(*args):
    args_list = list(args)
    args_list[1].sort()
    args_list[1] = list(set(args_list[1]))
    args_list[1].reverse()
    args_list[1] = [x for x in args_list[1] if x <= args_list[0]]
    result = args_list[1]
    return result


def calc_path(*args):
    args_list = list(args)
    amount = args_list[0]
    coins = args_list[1]

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
    C = [3, 2, 4, 5, 8, 6, 1, 6, 2]
    N = 5
    C = clean_up(N, C)
    print(C)
    C_paths = calc_path(N, C)
    print(C_paths)
