# https://projecteuler.net/problem=10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
import math


def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_prime_factors(v):

    i = 2
    f = []

    while i < v:
        # print(i)
        if is_prime(i):
            f.append(i)
        i += 1

    return f


factors = find_prime_factors(2000000)
# print(factors)
res = sum(factors)
print(res)
