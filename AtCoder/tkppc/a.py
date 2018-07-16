# https://tkppc.contest.atcoder.jp/tasks/tkppc2015_a

N = int(input())

A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

for a, b in zip(A, B):
    print(a + b)

