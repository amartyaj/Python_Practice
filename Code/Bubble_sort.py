#!/usr/bin/env python3

def sort_arr(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    my_arr = [5, 6, 3, 4, 9, 8, 2, 1]
    my_sorted_array = sort_arr(my_arr)
    print(my_sorted_array)
