# https://projecteuler.net/problem=5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def get_prime_factors(value):
    dic = {}

    i = 2
    n = value
    while i <= n:
        while n % i == 0:
            n /= i
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        i += 1

    return dic


dic = {}
for i in range(20):
    res = get_prime_factors(i)
    for key, value in res.iteritems():
        if key in dic:
            dic[key] = value if dic[key] < value else dic[key]
        else:
            dic[key] = value

result = 1
for key, value in dic.iteritems():
    result *= key ** value

print(result)
