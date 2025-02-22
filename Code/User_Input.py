#!/usr/bin/env python

import re

def clean_up(string):
    pattern = "^[a-zA-Z]+"
    result = re.search(pattern, string)
    return result.group(0)

if __name__ == "__main__":
    while True:
        name = input("Please enter your first name: ")
        if name:
            break
        else:
            print("Input cannot be empty, please try again ..")

    name = clean_up(name)
    print(name)
