
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


def get_prime_factors(n):
    d = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            d.append(i)
            while n != i:
                n /= i
        i += 1
    return d



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


# split integer to list

def split_int(n):
    return list(map(int, list(str(n))))

#####################################################

print(split_int(12345))

print(is_prime(2))