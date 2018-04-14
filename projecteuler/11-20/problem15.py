# https://projecteuler.net/problem=15


def permutuation(n):
    if n == 1: return 1
    return n * permutuation(n - 1)


def combi(a, c):
    x = permutuation(a)
    y = permutuation(a-c)
    z = permutuation(c)
    return x / (y * z)

# print(combi(4, 2))
print(combi(40, 20))
