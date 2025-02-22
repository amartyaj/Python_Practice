#!/usr/bin/env python

def calc_fib(n):
    if n < 0:
        result = None
        return result
    elif n == 0:
        result = n
        return result
    elif n == 1:
        result = 1
        return result
    else:
        result = calc_fib(n - 2) + calc_fib(n - 1)
        return result

if __name__ == "__main__":
    # print("Test")
    for i in range(0, 10):
        fib = calc_fib(i)
        print(f"{i + 1}th number in Fibonacci series is: {fib}")
