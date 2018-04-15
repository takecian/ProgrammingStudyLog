# create sample data
import random
n = 10**1

print(n)

d = []
for i in range(n):
    d.append(str(random.randint(0, 10**9)))

print(" ".join(d))


# input

count = int(input())    # number of input
for i in range(count):  # loop for each input
    data = input()
    # do something


# calculate prime factors


def get_prime_factors(n):
    d = []
    i = 2
    while i * i < n:
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
            if i != n / i:
                d.append(n / i)
        i += 1
    return d


