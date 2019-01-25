# https://projecteuler.net/problem=21
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.


def sum_divisors(n):
    d = []
    i = 1
    while i < n:
        if n % i == 0:
            d.append(i)
        i += 1
    # print(d)
    # print(sum(d))
    return sum(d)

def is_amicable(n):
    d = sum_divisors(n)
    dd = sum_divisors(d)
    return dd == n and n != d

# print(is_amicable(6))


res = 0
for i in range(1, 10000):
    if is_amicable(i):
        print(i)
        res += i
print(res)