# https://atcoder.jp/contests/abc103/tasks/abc103_d


N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(M)]

a.sort(key=lambda x: x[1])

# print(a)

count = 0

g = 0
for p in a:
    if g <= p[0]:
        count += 1
        g = p[1]
        # print(p)

print(count)
