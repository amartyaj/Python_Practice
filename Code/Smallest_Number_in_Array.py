#!/usr/bin/env python

# Find the Kth smallest element from an array.
# Assumption: All the elements in the array are positive natural numbers

def clean_up(arr):
    arr = list(set(arr))
    return arr

def calc_min(pos, arr):
    if (pos - 1) > len(arr):
        return arr[-1]
    result = arr[pos - 1]
    return result

if __name__ == "__main__":
    array = [1, 2, 4, 4, 10, 3, 7, 6, 101, 108, 110]
    K = 100
    array = clean_up(array)
    min_num = calc_min(K, array)
    # print(array)
    print(min_num)
