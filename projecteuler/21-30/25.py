# https://projecteuler.net/problem=25
import sys

cache = {0: 1, 1: 1, 2: 1}


def fib(n):
    if n in cache:
        return cache[n]
    cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]


for i in range(sys.maxsize):
    if len(str(fib(i))) == 1000:
        print(i)
        break

