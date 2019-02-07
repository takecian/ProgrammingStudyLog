# https://atcoder.jp/contests/abc054/tasks/abc054_c
import itertools


N, M = map(int, input().split())

C = [list(map(int, input().split())) for _ in range(M)]

seq = [i + 1 for i in range(1, N)]
# print(list(itertools.permutations(seq)))

count = 0
for l in itertools.permutations(seq):
    # print(l)
    connected = True
    for i in range(len(l) - 1):
        a = min(l[i], l[i+1])
        b = max(l[i], l[i+1])
        if i == 0 and [1, l[i]] not in C:
            connected = False
            break
        if [a, b] not in C:
            connected = False
            break
    if connected:
        # print(l)
        count += 1

print(count)
