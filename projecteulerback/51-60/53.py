# https://projecteuler.net/problem=53


cache = {0:0, 1:1, 2:2, 3:6}


def permutation(n):
    if n in cache:
        return cache[n]
    cache[n] = n * permutation(n - 1)
    return cache[n]


def combination(n, r):
    return permutation(n) // (permutation(r) * permutation(n-r))


count = 0
for n in range(1, 101):
    for r in range(1, n):
        val = combination(n, r)
        if val > 1000000:
            count += 1
            print("n = " + str(n) + "r = " + str(r) + ", comb = " + str(val))

print(count)