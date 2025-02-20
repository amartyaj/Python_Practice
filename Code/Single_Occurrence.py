#!/usr/bin/env python

# Find the single occurring element in an array in which all other elements are occurring twice.

def clean_up(arr):
    arr.sort()
    return arr

def find_single_element(arr):
    dict = {}
    for x in arr:
        if x in dict:
            dict[x] += 1
        else:
            dict.update({x: 1})
    for i, j in dict.items():
        if j == 1:
            return i

    return result

if __name__ == "__main__":
    array = [1, 1, 2, 2, 3, 4, 5, 3, 4]
    array = clean_up(array)
    # print(array)
    single_element = find_single_element(array)
    print(single_element)
