# https://atcoder.jp/contests/abc113/tasks/abc113_c

N, M = map(int, input().split())
c_l = [[int(i) for i in input().split()] + [j] for j in range(M)]

# print(c_l)
c_l.sort(key=lambda x: x[1])

counter = [0] * (N+1)
for c in c_l:
    p = c[0]
    counter[p] += 1
    c.append("{:06}{:06}".format(c[0], counter[p]))

c_l.sort(key=lambda x: x[2])

for c in c_l:
    print(c[3])

