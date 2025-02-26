#!/usr/bin/env python3

if __name__ == "__main__":
    long_string = "Line_1_Word_1 " "Line_1_Word_2\n" "Line2_Word_1"
    """
    This also works:
    long_string = ("Line_1_Word_1 "
                   "Line_1_Word_2\n"
                   "Line_2_Word_1")
    """
    print(long_string)

    long_string2_part1 = "Line1: Word1 Word2 "
    long_string2_part2 = "Word3"
    long_string2_part3 = "\nLine2: Word1 Word2"

    long_string2 = long_string2_part1 + long_string2_part2 + long_string2_part3
    print(long_string2)

    long_string3 = "Line1: Word1 \
                    Word2\n\
                    Line2: Word1 Word2"
    print(long_string3)

    long_string4 = """Line1: Word1 Word2
                      Line2: Word1"""
    print(long_string4)

    long_string5 = """Line1: Word1 Word2
Line2: Word1"""
    print(long_string5)
