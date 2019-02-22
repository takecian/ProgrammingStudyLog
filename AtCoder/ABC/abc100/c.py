# https://abc100.contest.atcoder.jp/tasks/abc100_c


def even_count(v):
    if v % 2 != 0:
        return 0
    else:
        r = 0
        while v % (2 ** 20) == 0:
            r += 20
            v //= (2 ** 20)

        while v % (2 ** 10) == 0:
            r += 10
            v //= (2 ** 10)

        while v % 2 == 0:
            r += 1
            v //= 2

    return r


N = int(input())

a = list(map(int, input().split()))

count = 0

for i in a:
    count += even_count(i)

print(count)
