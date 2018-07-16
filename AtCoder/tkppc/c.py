# https://tkppc.contest.atcoder.jp/tasks/tkppc2015_c

N, M = map(int, input().split())
S = int(input())

T = [0 for _ in range(10000)]

for _ in range(N):
    t, k = map(int, input().split())
    T[t-1] = k

# print(T)

total = 0
d = 0
for i in range(S - 1):
    total += T[i]
    if total >= M:
        d += 1

print(d)
