# https://projecteuler.net/problem=31

coins = [200, 100, 50, 20, 10, 5, 2, 1]


def made_up(cl, v):
    if len(cl) == 0:
        return 0
    total = 0
    c = cl.pop(0)
    i = 0
    while c * i <= v:
        if c * i < v:
            tv = v - c * i
            total += made_up(list(cl), tv)
        if c * i == v:
            total += 1
            break
        i += 1
    return total


print(made_up(coins, 200))
