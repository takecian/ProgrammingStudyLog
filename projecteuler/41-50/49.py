# https://projecteuler.net/problem=49

import itertools


def is_prime(n):
    if 2 > n: return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for comb in list(itertools.combinations_with_replacement(d, 4)):
    l = []
    for p in list(itertools.permutations(comb, 4)):
        v = p[0] * 1000 + p[1] * 100 + p[2] * 10 + p[3]
        if v > 999 and is_prime(v) and v not in l:
            l.append(v)

    if len(l) > 2:
        # print(comb)
        # print(l)
        l = sorted(l)
        for a in range(len(l)-2):
            for b in range(a+1, len(l) - 1):
                for c in range(b+1, len(l)):
                    if l[b] - l[a] == l[c] - l[b]:
                        print(l)
                        print("answer = " + str(l[a]) + str(l[b]) + str(l[c]) + ", diff = " + str(l[b] - l[a]))

