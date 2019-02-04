# https://beta.atcoder.jp/contests/abs/tasks/abc087_b


def calc_c(c, x):
    # print(str(c) + ", " + str(x))
    for i in range(c+1):
        if x == 50 * i:
            return 1

    return 0


def calc_b(b, c, x):
    pattern = 0

    i = 0
    while x - 100 * i >= 0 and i <= b:
        if x - 100 * i > 0:
            pattern += calc_c(c, x - 100 * i)
        if x - 100 * i == 0:
            pattern += 1
        i += 1
    # print(pattern)
    return pattern


def calc_a(a, b, c, x):
    pattern = 0

    i = 0
    while x - 500 * i >= 0 and i <= a:
        if x - 500 * i > 0:
            pattern += calc_b(b, c, x - 500 * i)
        if x - 500 * i == 0:
            pattern += 1
        i += 1
    print(pattern)


a = int(input())
b = int(input())
c = int(input())

x = int(input())


calc_a(a, b, c, x)