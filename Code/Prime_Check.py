#!/usr/bin/env python3

import math as m


def run_prime_check(num):
    result = num
    if num <= 1:
        result = None
    elif num == 2:
        result = 2
    else:
        for i in range(2, m.ceil(m.sqrt(num)) + 1):
            # print(f"**{i}**")
            if (num % i) == 0:
                result = None
                break
    return result


if __name__ == "__main__":
    # print("Test")
    my_nums = list(range(0, 12))

    for my_num in my_nums:
        prime_num = run_prime_check(my_num)
        if prime_num != None:
            print(prime_num)
