# https://beta.atcoder.jp/contests/abc085/tasks/abc085_c

N, Y = map(int, input().split())


def solve(n, y):
    for a in range(N + 1):
        rest = y - 10000 * a
        if rest == 0:
            return (a, 0, 0)
        bc = n - a
        cand_b = rest // 1000


    return (-1, -1, -1)


result = solve(N, Y)
print(str(result[0]) + ' ' + str(result[1]) + ' ' + str(result[2]))
