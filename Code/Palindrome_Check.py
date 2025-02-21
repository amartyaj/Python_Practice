#!/usr/bin/env python

# String Palindrome Check

def palindrome_check1(my_word1):
    result = False
    if my_word1 == ''.join(reversed(list(my_word1))):
        result = True
    return result

def palindrome_check2(my_word2):
    result = False
    my_len = len(my_word2)
    my_word2 = list(my_word2)
    my_reversed_word = my_word2.copy()
    for i in range(0, my_len):
        my_reversed_word[i] = my_word2[my_len -1 - i]
    if ''.join(my_word2) == ''.join(my_reversed_word):
        result = True
    return result
        

if __name__ == "__main__":
    words_array = ["", "abc", "abcba", "abccba"]
    for word in words_array:
        print(f"*{word}* -> ", end="")
        print(f"{palindrome_check1(word)} -> ", end="")
        print(palindrome_check2(word))
