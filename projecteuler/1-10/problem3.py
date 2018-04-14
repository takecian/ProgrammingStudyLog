# https://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


def get_prime_factor(value):
    i = 2
    n = value
    while i * i <= n:  # To be able to divide n with i, n should be larger than i * i
        while n % i == 0 and n != i:
            n = n / i  # reduce target value by dividing divisor
        i = i + 1
    return n


result = get_prime_factor(600851475143)
print(result)
