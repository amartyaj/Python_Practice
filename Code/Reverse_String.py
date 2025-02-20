#!/usr/bin/env python

import re

# Reverse a string without altering the position of any special characters
# present in the string

def reverse_string(my_str):
    # result = my_str[::-1]
    pattern1 = "[a-zA-Z0-9]"
    pattern2 = "[^a-zA-Z0-9]"
    my_str_no_special_chars = re.findall(pattern1, my_str)
    my_str_no_special_chars_rev = reversed(my_str_no_special_chars)
    my_str_no_special_chars_rev = ''.join(my_str_no_special_chars_rev)
    my_str_no_special_chars_rev = list(my_str_no_special_chars_rev)
    i = -1
    for my_string in my_str:
        i += 1
        if re.match(pattern2, my_string):
            my_str_no_special_chars_rev.insert(i, my_string)
    my_str_no_special_chars_rev = ''.join(my_str_no_special_chars_rev)
    result = my_str_no_special_chars_rev
    return result

if __name__ == "__main__":
    # print("Test")

    strings = ['', 'AbracadabRa', 'xyz123$ff%', 'Test123#Hello$World', 'abc$d$e$', 'ab d $$ t']
    for string in strings:
        reversed_string = reverse_string(string)
        print(f"{string} -> ", end="")
        print(reversed_string)
