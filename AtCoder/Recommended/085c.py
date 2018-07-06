# https://beta.atcoder.jp/contests/abc085/tasks/abc085_c

N, Y = map(int, input().split())


def solve(n, y):
    for a in range(n + 1):
        rest = y - 10000 * a
        if rest < 0:
            break
        if rest == 0 and a == n:
            return a, 0, 0

        bc = n - a
        all_c = 1000 * bc
        rest = rest - all_c
        if rest >= 0 and rest % 4000 == 0:
            b = rest // 4000
            c = bc - b
            if b >= 0 and c >= 0:
                return a, b, c

    return -1, -1, -1


result = solve(N, Y)
print(str(result[0]) + ' ' + str(result[1]) + ' ' + str(result[2]))
