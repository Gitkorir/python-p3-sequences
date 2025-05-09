#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    fib = [0,1] #initialize the first two fibonnaci numbers

    while len(fib) < length:
        next_number = fib[-1] + fib[-2]
        fib.append(next_number)
    print(fib[:length])    