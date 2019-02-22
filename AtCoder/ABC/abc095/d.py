# https://arc096.contest.atcoder.jp/tasks/arc096_b


def inp(): return map(int, input().split())


N, C = inp()
l = [tuple(inp()) for _ in range(N)]

r1 = [0] * N
r2 = [0] * N
l1 = [0] * N
l2 = [0] * N

cal = 0
ans1 = 0
ans2 = 0
for i, (x, v) in enumerate(l):  # clockwise
    cal += v
    ans1 = max(ans1, cal - x)
    ans2 = max(ans2, cal - 2 * x)
    r1[i] = ans1
    r2[i] = ans2

cal = 0
ans1 = 0
ans2 = 0
for i, (x, v) in enumerate(l[::-1]):  # counter clockwise
    x = C - x
    cal += v
    ans1 = max(ans1, cal - x)
    ans2 = max(ans2, cal - 2 * x)
    l1[-1 - i] = ans1
    l2[-1 - i] = ans2

ans = 0

for i in range(N - 1):
    ans = max(ans, r2[i] + l1[i + 1], r1[i] + l2[i + 1])

ans = max(ans, r1[-1], l1[0])
print(ans)

