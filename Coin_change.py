# Knapsack Practice: Coin change

def clean_up(num, list):
    list.sort()
    list.reverse()
    list = [x for x in list if x <= num]
    return list

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

if __name__ == '__main__':
    N = 5
    C = [3, 2, 8, 5, 1, 6]
    C = clean_up(N, C)
    print(calc_path(N, C))
