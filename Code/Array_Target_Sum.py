#!/usr/bin/env python

# Find 2 numbers from an array whose sum is equal to the target sum.
# Assumption: All numbers in the array are unique and positive natural numbers.

def clean_up(arr):
    arr = list(set(arr))
    return arr

def calc_path(target, array, max_elements):
    def backtrack(target, start, path, result):
        if len(path) > max_elements:
            return
        if target == 0:
            result.append(path)
            return
        
        for i in range(start, len(array)):
            if array[i] > target:
                continue
            backtrack(target - array[i], i, path + [array[i]], result)
    
    start = 0
    path = []
    result = []
    backtrack(target, start, path, result)
    return result

if __name__ == "__main__":
    array = [1, 2, 3, 3, 4, 5, 6, 6, 8]
    target = 5
    max_array_elements = 2

    array = clean_up(array)
    path = calc_path(target, array, max_array_elements)
    print(path)
    final_path = []
    for element in path:
        unique_elements = list(set(element))
        if len(unique_elements) == max_array_elements and unique_elements == element:
            final_path.append(element)
    print(final_path)
