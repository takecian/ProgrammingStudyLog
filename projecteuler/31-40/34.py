# https://projecteuler.net/problem=34

cache = {0: 1, 1: 1, 2: 2}


def permutation(n):
    if n in cache:
        return cache[n]
    cache[n] = n * permutation(n - 1)
    return cache[n]


#   999999(6digits) -> 9!*6=2177280(7digits)
#  9999999(7digits) -> 9!*7=2540160(7digits)
# 99999999(8digits) -> 9!*8=2903040(7digits)

total = 0
for i in range(10, 2540160):
    l = list(map(int, list(str(i))))
    # print(l)
    v = 0
    for m in l:
        v += permutation(m)

    # print(str(i) + ", " + str(v))
    if i == v:
        print(str(i) + ", " + str(v))
        total += i

print(total)

