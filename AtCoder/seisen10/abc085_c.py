# https://atcoder.jp/contests/abc085/tasks/abc085_c

N, Y = map(int, input().split())


def calc(n, y):
    for i in range(n + 1):
        rest = y - i * 10000
        for j in range(n - i + 1):
            if rest - (j * 5000) == (n - i - j) * 1000:
                return i, j, n - i - j
    return -1, -1, -1

result = calc(N, Y)
print('%d  %d %d' % (result[0], result[1], result[2]))
