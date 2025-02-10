#!/Users/Jimi/anaconda3/bin/python

def clean_up(total, coin_list):
    coin_list.sort()
    coin_list.reverse()
    coin_list = [x for x in coin_list if x <= total]
    return coin_list

def find_ways(amount, coins):
    
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
    N = 3
    C = [3, 2, 6, 8, 1]
    C = clean_up(N, C)
    print(find_ways(N, C))
