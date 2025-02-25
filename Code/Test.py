#!/usr/bin/env python


def classify(word):
    result = ""

    if word == "Word 1":
        result = "Good word"
    elif word == "Word 2":
        result = "Bad word"
    else:
        result = "Neutral word"

    return result


if __name__ == "__main__":

    my_words = ["Word 1", "Word 2", "Word 3"]

    for my_word in my_words:
        my_result = classify(my_word)
        print(my_result)
        # print(help(print))
