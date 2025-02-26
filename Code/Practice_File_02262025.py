#!/usr/bin/env python3


def clean_up(*args):
    pass
    # print(args[0])
    # print(args[1])
    my_amount = args[0]
    my_coins = list(args[1])
    # print(my_coins)
    my_coins.sort()
    # print(my_coins)
    my_coins = list(set(my_coins))
    # print(my_coins)
    my_coins.reverse()
    # print(my_coins)
    my_coins = [x for x in my_coins if x <= my_amount]
    # print(my_coins)
    result = my_coins
    return result


def calc_path(*args):
    pass
    amount = args[0]
    coins = list(args[1])

    def backtrack(target, start, path, result):
        if target == 0:
            result.append(path)
            return result

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
    pass

    N = 5
    C = [1, 2, 3, 4, 5, 6, 9, 8, 7, 3, 4]
    C = clean_up(N, C)
    # print(C)
    paths = calc_path(N, C)
    print(paths)
