# https://projecteuler.net/problem=55


def calc(n):
    r = int(str(n)[::-1])
    return n + r


def is_palindromic(n):
    return str(n) == str(n)[::-1]


count = 0
for i in range(1, 10001):
    is_p = False

    v = i
    for j in range(50):
        v = calc(v)
        if is_palindromic(v):
            print(str(i) + ", pand = " + str(v))
            is_p = True
            break
    if is_p:
        count += 1

print(10000 - count)