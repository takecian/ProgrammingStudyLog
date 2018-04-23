
# create sample data

import random

def random_data():
    n = 10**1

    print(n)

    d = []
    for i in range(n):
        d.append(str(random.randint(0, 10**9)))

    print(" ".join(d))


# input

def read_input():
    count = int(input())    # number of input
    for i in range(count):  # loop for each input
        data = input()
        # do something


# calculate prime factors


def get_prime_factors_list(n):
    d = []
    i = 2
    while i <= n:
        while n % i == 0:
            d.append(i)
            n //= i
        i += 1
    return d


def get_primes_dic(v):
    m = {}
    i = 2

    while i <= v:
        while v % i == 0:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
            v //= i

        i += 1

    return m

# calculate divisors


def get_divisors(n):
    d = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            d.append(i)
            q = int(n / i)
            if i != q:
                d.append(q)
        i += 1
    return d


# Check wheather n is prime or not

def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True

# Format

def f(n):
    number = 50
    number_padded = '%04d' % number
    print(number_padded)

# split integer to list

def split_int(n):
    return list(map(int, list(str(n))))


def reverse_int(n):
    return list(map(int, list(str(n))[::-1]))


# read
def read_input1():
    a, b, c, x, y = map(int, input().split())

# read
def inp(): return map(int, input().split())
def read_input2():
    n, s = inp()
    l = [tuple(inp()) for _ in range(n)]

#####################################################

print(get_prime_factors_list(2180))
print(get_primes_dic(2180))

print(split_int(12345))

print(reverse_int(12345))

print(is_prime(2))