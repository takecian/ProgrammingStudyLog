# https://projecteuler.net/problem=56


def calc_sum(n):
    return sum(map(int, list(str(n))))


m = 0
for a in range(1, 100):
    for b in range(1, 100):
        val = calc_sum(a ** b)
        if val > m:
            m = val
print(m)
