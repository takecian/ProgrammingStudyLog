# https://projecteuler.net/problem=57


def f(n, d):
    return n + d + d, n + d


num = 3
den = 2

count = 0
for i in range(1000):
    num, den = f(num, den)
    # print(str(num) + "/" + str(den))
    if len(str(num)) > len(str(den)):
        count += 1

print(count)
