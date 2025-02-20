#!/usr/bin/env python

def clean_up(amount, arr):
    arr.sort()
    arr.reverse()
    arr = [x for x in arr if x <= amount]
    return arr

def calculate_path(amount, arr):
    def backtrack(target, coins, path, result):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(arr)):
            if arr[i] > target:
                continue
            backtrack(target - arr[i], i, path + [arr[i]], result)
        
    start = 0
    path = []
    result = []
    backtrack(amount, start, path, result)
    return result

if __name__ == "__main__":
    N = 5
    C = [3, 2, 4, 8, 5, 1]
    print(C)
    C = clean_up(N, C)
    print(C)
    C_Paths = calculate_path(N, C)
    print(C_Paths)