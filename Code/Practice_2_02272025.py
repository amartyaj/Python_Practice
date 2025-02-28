#!/usr/bin/env python3

if __name__ == "__main__":
    pass

    my_list = ["xyz", "xy", "x", "xx", "def", "abc", "xxx", "abcd"]
    max_word_length = 0
    for word in my_list:
        if len(word) > max_word_length:
            max_word_length = len(word)
    print(max_word_length)

    my_list.sort()

    print(my_list)

    my_string = "yyxxzzaacb"
    my_string_list = []
    for char in my_string:
        my_string_list.append(char)
    print(my_string_list)

    for i in range(0, len(my_string_list)):
        for j in range(i, len(my_string_list)):
            print(i, j)
            if ord(my_string_list[i]) > ord(my_string_list[j]):
                my_string_list[i], my_string_list[j] = (
                    my_string_list[j],
                    my_string_list[i],
                )
        print(my_string_list)

    # print(my_string_list)
    my_string = "".join(my_string_list)
    print(my_string)
