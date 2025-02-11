#!/usr/bin/env python3

import random

if __name__ == "__main__":
    my_list = list(range(1, 10, 1))
    my_dict = {}

    for i in range(1, 50, 1):
        random_power = random.randrange(5)
        random_index = random.randrange(len(my_list))
        my_key = str(my_list[random_index]) + '_' + str(random_power)
        print(f"{my_list[random_index]} ^ {random_power} -> ", end="")
        
        cached_value = my_dict.get(my_key)
        
        if cached_value != None:
            my_value = cached_value
            print(f"Found in cache: {cached_value}")
        else:
            my_value = my_list[random_index] ** random_power
            print(f"Calculated value: {my_value}")
            my_dict.update({my_key: my_value})
