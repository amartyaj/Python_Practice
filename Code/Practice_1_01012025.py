#!/usr/bin/env python3


def uppercase(func):
    # print("Entering decorator")
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    # return func
    return wrapper


@uppercase
def greet():
    return "Hello"


if __name__ == "__main__":
    pass

    print(type(greet))
    print(greet)
    print(uppercase)
    result = greet()
    print(result)
