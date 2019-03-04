# https://agc023.contest.atcoder.jp/tasks/agc023_a

import math


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def convert_map(l):
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


N = list(map(int, input()))[0]

li = list(map(int, input().split()))

counter = [0]
for i in li:
    counter.append(counter[-1] + i)

# print(counter)

d = convert_map(counter)

# print(d)

patterns = 0
for key, value in d.items():
    if value >= 2:
        patterns += combinations_count(value, 2)

print(patterns)
