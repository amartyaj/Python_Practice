#!/usr/bin/env python

import math as m

def calc_divisor(T, M):
    unique_array = list(set(M))
    if len(unique_array) == 1 and unique_array[0] == 0:
        return "Undefined"
    
    for i in range(1, T + 1):
        sum = 0
        for j in M:
            sum += m.ceil(j / i)
            if sum > T:
                break
        if sum <= T:
            return i
                
    return None

if __name__ == "__main__":
    threshold = 10
    my_array = [1, 7, 6, 9, 9, 4, 2, 6]
    divisor = calc_divisor(threshold, my_array)
    print(divisor)
    threshold = 6
    my_array = [1, 2, 5, 9]
    divisor = calc_divisor(threshold, my_array)
    print(divisor)
    threshold = 1
    my_array = [1, 7, 6, 9, 9, 4, 2, 6]
    divisor = calc_divisor(threshold, my_array)
    print(divisor)
    threshold = 10
    my_array = [0, 0, 0, 0, 0]
    divisor = calc_divisor(threshold, my_array)
    print(divisor)
    threshold = 1
    my_array = [1, 0, 1, 0, 0]
    divisor = calc_divisor(threshold, my_array)
    print(divisor)
