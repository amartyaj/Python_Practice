#!/usr/bin/env python

# Find the k-th element in a list

def find_element(pos, array):
    if pos <= 0:
        result = None
    elif pos <= len(array):
        result = array[pos - 1]
    else:
        result = None
    return result

if __name__ == "__main__":
    # print("Test")
    arr = [1, 3, 5, 7, 2, 4, 6, 8, 9]

    # Giving k the value -1 to 10 in this case so that all cases are covered:
    for k in range(-1, (len(arr) + 2)):
        element = find_element(k, arr)
        print(element)
